import json

import pika

from src.domain.dataclasses.AnalysisQuery import AnalysisQuery
from src.domain.repositories.SendAnalysisRepository import SendAnalysisRepository
from src.infrastructure.rabbitmq import get_connection_parameters


class SendAnalysisToRabbitMQ(SendAnalysisRepository):
    def send_analysis(self, analysis_query_to_send: AnalysisQuery) -> None:
        connection: pika.adapters.BlockingConnection = pika.BlockingConnection(parameters=get_connection_parameters())
        channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

        channel.confirm_delivery()

        try:
            channel.basic_publish(
                exchange='test',
                routing_key='test',
                body=json.dumps({
                    'analysis_id': analysis_query_to_send.analysis_id,
                    'bias_code': analysis_query_to_send.bias_code,
                    'algorithm_code': analysis_query_to_send.algorithm_code,
                    'data_set_source': analysis_query_to_send.data_set_source
                }),
                properties=pika.BasicProperties(
                    content_type='application/json',
                    delivery_mode=2
                ),
                mandatory=True
            )
        except pika.exceptions.UnroutableError:
            # TODO Handle error
            pass
        finally:
            channel.close()
            connection.close()

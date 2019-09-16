import json
import uuid

import pika

from src.domain.dataclasses.AnalysisResult import AnalysisResult
from src.infrastructure.rabbitmq import get_connection_parameters
from src.infrastructure.repositories.AnalysisResultFromMongoDB import AnalysisResultFromMongoDB


def store_analysis_when_finished():
    def on_message(message_channel, method_frame, header_frame, body):
        dict_message = json.loads(body)
        AnalysisResultFromMongoDB().store(
            AnalysisResult(
                resultAnalysisId=str(uuid.uuid4()),
                analysisId=dict_message['analysis_id'],
                algorithmBiasGraph=dict_message['algorithm_bias'],
                dataBiasGraph=dict_message['data_bias']
            )
        )
        message_channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    connection: pika.adapters.BlockingConnection = pika.BlockingConnection(parameters=get_connection_parameters())
    channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()
    channel.basic_consume('test2', on_message, consumer_tag='backend')
    try:
        channel.start_consuming()
    except:
        channel.stop_consuming()
    connection.close()

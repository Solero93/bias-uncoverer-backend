import json
import uuid

import pika

from src.domain.dataclasses.AnalysisResult import AnalysisResult
from src.infrastructure.rabbitmq import get_connection_parameters
from src.infrastructure.repositories.AnalysisResultFromMongoDB import AnalysisResultFromMongoDB


def store_analysis_when_finished():
    connection: pika.adapters.BlockingConnection = pika.BlockingConnection(parameters=get_connection_parameters())
    channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

    for method_frame, properties, body in channel.consume(queue='test2', auto_ack=True):
        print('lel')
        dict_message = json.loads(body)
        print(dict_message)
        AnalysisResultFromMongoDB().store(
            AnalysisResult(
                resultAnalysisId=str(uuid.uuid4()),
                analysisId=dict_message['analysis_id'],
                algorithmBiasGraph=dict_message['algorithm_bias'],
                dataBiasGraph=dict_message['data_bias']
            )
        )

    connection.close()

import json

import pika

from src.dataclasses.AnalysisQuery import AnalysisQuery


def send_analysis(analysis_query_to_send: AnalysisQuery):
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    parameters = pika.ConnectionParameters(credentials=credentials)
    connection: pika.adapters.BlockingConnection = pika.BlockingConnection(parameters=parameters)
    channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

    channel.confirm_delivery()
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
            delivery_mode=1
        ),
        mandatory=True
    )

    channel.close()
    connection.close()

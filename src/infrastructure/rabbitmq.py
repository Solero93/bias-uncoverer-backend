import pika


def get_connection_parameters() -> pika.ConnectionParameters:
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    return pika.ConnectionParameters(credentials=credentials)

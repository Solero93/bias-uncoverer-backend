import pika


def get_connection_parameters() -> pika.ConnectionParameters:
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    return pika.ConnectionParameters(host='rabbit', credentials=credentials)


def get_blocking_connection() -> pika.adapters.BlockingConnection:
    return pika.BlockingConnection(parameters=get_connection_parameters())

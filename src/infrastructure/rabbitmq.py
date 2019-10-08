from time import sleep

import pika


def get_connection_parameters() -> pika.ConnectionParameters:
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    return pika.ConnectionParameters(host='rabbit', credentials=credentials)


def get_blocking_connection() -> pika.adapters.BlockingConnection:
    return pika.BlockingConnection(parameters=get_connection_parameters())


def wait_for_connection_to_be_open_or_exit():
    wait_time = 1
    success = False

    while wait_time < 100 and not success:
        try:
            connection: pika.adapters.BlockingConnection = get_blocking_connection()
            connection.close()
            success = True
        except pika.connection.exceptions.AMQPConnectionError:
            sleep(wait_time)
            wait_time *= 2

    if not success:
        print("Couldn't connect to rabbit")
        exit(1)

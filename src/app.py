from multiprocessing import Process
from time import sleep

import pika
from flask import Flask

from src.infrastructure.endpoints.algorithms import algorithms_blueprint
from src.infrastructure.endpoints.analysis import analysis_blueprint
from src.infrastructure.endpoints.bias import bias_blueprint
from src.infrastructure.endpoints.file import file_blueprint
from src.infrastructure.endpoints.results import results_blueprint
from src.infrastructure.rabbitmq import get_blocking_connection
from src.infrastructure.store_analysis_when_finished import store_analysis_when_finished

app = Flask(__name__)

app.register_blueprint(algorithms_blueprint)
app.register_blueprint(analysis_blueprint)
app.register_blueprint(bias_blueprint)
app.register_blueprint(file_blueprint)
app.register_blueprint(results_blueprint)

if __name__ == '__main__':
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

    p = Process(target=store_analysis_when_finished)
    p.start()

    app.run(host='0.0.0.0', port=5000)

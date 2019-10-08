from multiprocessing import Process

from flask import Flask

from src.infrastructure.endpoints.algorithms import algorithms_blueprint
from src.infrastructure.endpoints.analysis import analysis_blueprint
from src.infrastructure.endpoints.bias import bias_blueprint
from src.infrastructure.endpoints.file import file_blueprint
from src.infrastructure.endpoints.results import results_blueprint
from src.infrastructure.rabbitmq import wait_for_connection_to_be_open_or_exit
from src.infrastructure.store_analysis_when_finished import store_analysis_when_finished

app = Flask(__name__)

app.register_blueprint(algorithms_blueprint)
app.register_blueprint(analysis_blueprint)
app.register_blueprint(bias_blueprint)
app.register_blueprint(file_blueprint)
app.register_blueprint(results_blueprint)

if __name__ == '__main__':
    wait_for_connection_to_be_open_or_exit()
    p = Process(target=store_analysis_when_finished)
    p.start()

    app.run(host='0.0.0.0', port=5000)

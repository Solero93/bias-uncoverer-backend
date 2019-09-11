import threading

from flask import Flask

from src.endpoints.algorithms import algorithms_blueprint
from src.endpoints.analysis import analysis_blueprint
from src.endpoints.bias import bias_blueprint
from src.endpoints.file import file_blueprint
from src.endpoints.results import results_blueprint
from src.rabbitmq.store_analysis_when_finished import store_analysis_when_finished

app = Flask(__name__)

app.register_blueprint(algorithms_blueprint)
app.register_blueprint(analysis_blueprint)
app.register_blueprint(bias_blueprint)
app.register_blueprint(file_blueprint)
app.register_blueprint(results_blueprint)

t = threading.Thread(name='child procs', target=store_analysis_when_finished)
t.start()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

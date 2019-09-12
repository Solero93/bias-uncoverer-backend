import threading

from flask import Flask

from src.infrastructure.endpoints.algorithms import algorithms_blueprint
from src.infrastructure.endpoints.analysis import analysis_blueprint
from src.infrastructure.endpoints.bias import bias_blueprint
from src.infrastructure.endpoints.file import file_blueprint
from src.infrastructure.endpoints.results import results_blueprint
from src.infrastructure.store_analysis_when_finished import store_analysis_when_finished

app = Flask(__name__)

app.register_blueprint(algorithms_blueprint)
app.register_blueprint(analysis_blueprint)
app.register_blueprint(bias_blueprint)
app.register_blueprint(file_blueprint)
app.register_blueprint(results_blueprint)

if __name__ == '__main__':
    t = threading.Thread(name='consume queue', target=store_analysis_when_finished)
    t.start()

    app.run(host='localhost', port=5000)

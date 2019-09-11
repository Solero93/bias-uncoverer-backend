from flask import Flask

from src.algorithms import algorithms_blueprint
from src.analysis import analysis_blueprint
from src.bias import bias_blueprint
from src.file import file_blueprint
from src.files import files_blueprint
from src.results import results_blueprint

app = Flask(__name__)

app.register_blueprint(algorithms_blueprint)
app.register_blueprint(analysis_blueprint)
app.register_blueprint(bias_blueprint)
app.register_blueprint(file_blueprint)
app.register_blueprint(files_blueprint)
app.register_blueprint(results_blueprint)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

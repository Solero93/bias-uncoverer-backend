FROM python:3.7

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Solero93/bias-uncoverer-algorithm.git /home/biasuncoverer_algorithm
WORKDIR /home/biasuncoverer_algorithm
RUN python setup.py install

ENTRYPOINT ["python", "-m", "src.main"]c
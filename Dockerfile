FROM python:3.7
COPY static /static
COPY templates /templates
COPY datasets /datasets
COPY setup.py setup.py
COPY src /src

RUN python setup.py install

ENTRYPOINT ["python", "-m", "src.app"]
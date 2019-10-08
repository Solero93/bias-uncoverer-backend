FROM python:3.7
COPY static /static
COPY templates /templates
COPY setup.py setup.py

RUN python setup.py install

COPY src /src

ENTRYPOINT ["python", "-m", "src.app"]
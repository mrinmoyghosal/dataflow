FROM localhost:32000/dataflow:v1
COPY test.py /usr/src/myapp/
COPY broker.py /usr/src/myapp/
COPY worker.py /usr/src/myapp/
WORKDIR /usr/src/myapp


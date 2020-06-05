FROM ubuntu:19.10

RUN apt-get update -y
RUN apt-get install -y  \
    openssl \
    software-properties-common \
    ca-certificates \
    wget \
    curl \
    ssh \
    git \
    build-essential \
    libtool \
    autoconf \
    automake \
    pkg-config \
    unzip \
    libkrb5-dev \
    cmake \
    python3-dev \
    python3-numpy-dev \
    python3-pip

RUN cd /tmp && git clone --depth 1 --branch v4.2.1 https://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make
RUN cd /tmp/libzmq && make install && ldconfig
RUN rm /tmp/* -rf

COPY app.py /usr/src/myapp/
COPY broker.py /usr/src/myapp/
COPY worker.py /usr/src/myapp/
COPY mgq.cpython-37m-x86_64-linux-gnu.so /usr/src/myapp/
WORKDIR /usr/src/myapp
RUN pip3 install flask
RUN ls
EXPOSE 9080
RUN python3 -c  "import mgq"

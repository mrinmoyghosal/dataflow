FROM ubuntu:latest

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
    
RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y
RUN apt-get install -y python3.7

RUN cd /tmp && git clone --depth 1 --branch v4.2.5 https://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make
RUN cd /tmp/libzmq && make install && ldconfig
RUN rm /tmp/* -rf

RUN python3 --version
RUN python3.7 --version
COPY test.py /usr/src/myapp/
COPY broker.py /usr/src/myapp/
COPY worker.py /usr/src/myapp/
COPY mgq.cpython-37m-x86_64-linux-gnu.so /usr/src/myapp/
WORKDIR /usr/src/myapp
RUN ls
EXPOSE 9080

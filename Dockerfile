FROM ubuntu:22.04

ENV USERNAME="devuser"

# Dependency Versions
ENV PYTHON_VERSION=3.10

# Update dependencies
RUN apt update && apt upgrade -y
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt install -y python${PYTHON_VERSION}
RUN apt-get -y install git

# Create developer user
RUN useradd -ms /bin/bash ${USERNAME}
USER ${USERNAME}
WORKDIR /home/${USERNAME}

# Clone git repository
RUN git clone https://github.com/jgo28/astoria.git
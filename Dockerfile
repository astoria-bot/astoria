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
    apt install -y python${PYTHON_VERSION} && \
    apt install -y python${PYTHON_VERSION}-venv && \
    apt-get install -y python3-pip && \
    apt-get -y install git

# Create developer user
RUN useradd -ms /bin/bash ${USERNAME}
USER ${USERNAME}
WORKDIR /home/${USERNAME}

# Copy over necessary files for astoria and install pip requirements
WORKDIR /home/${USERNAME}/astoria/
COPY requirements.txt ./
COPY ./bot bot
COPY .env .env
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "bot/bot.py"]

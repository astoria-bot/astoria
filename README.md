# Astoria: A Discord Bot

A simple Discord bot built with discord.py. Astoria currently is written
in Python 3.10.6.

## Resources
- [Discord.py](https://discordpy.readthedocs.io/en/stable/index.html)
- [Discord developer docs](https://discord.com/developers/docs/intro)

## Requirements
- [Docker](https://www.docker.com/)
- [MySQL](https://www.mysql.com/)

## Installation

### Docker Container
The bot can be run within the Docker container. The Docker container has the dependencies to run the bot.
#### Build Docker Image
```
make docker-build
```
#### Run Docker Image
```
make docker-run
```

### Testing via locally
If you want to do testing on your machine, you can set up a Python virtual environment:
#### Setup virtual environment

```
python3 -m venv astoria-env
source astoria-env/bin/activate
python3 -m pip install -r requirements.txt
```

### Connecting to Discord
Create a `.env` file in the following format:

```
DISCORD_TOKEN=${TOKEN}
DISCORD_GUILD=${GUILD}
CHANNEL_ID=${CHANNEL_ID}
```
Make sure you have developer mode enabled on Discord to obtain the guild and channel id values.

The token value is obtained from https://discord.com/developers/applications from the astoria
bot application.

### Connecting to the Database
TODO: Needs to be updated

Add to your `.env` file:

```
USERNAME=${USERNAME}
PASSWORD=${PASSWORD}
DATABASE=${DATABASE_NAME}
HOST=${HOST_IP}
```

## Starting/Stopping the MySQL database

```
make start-mysql
make stop-mysql
```
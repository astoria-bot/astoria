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
docker build --tag "astoria" .
```
#### Run Docker Image
```
docker run --rm -it  astoria:latest 
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

## Commands

### General

| Name | Description               | Usage |
|------|---------------------------|-------|
| help | Shows a list of commands. | !help |
| about | Displays a description about the bot. | !about |

### Moderation

| Name   | Description                                               | Usage                      |
|--------|-----------------------------------------------------------|----------------------------|
| kick   | Kicks a user from the server.                             | !kick [user]               |
| ban    | Bans a user from the server.                              | !ban [user]                |
| unban  | Unbans a user from the server.                            | !unban [user]              |
| role   | Gives/Removes a role from a user.                         | !role [user] [role]        |
| mute   | Mutes a user from text channels.                          | !mute [user]               |
| unmute | Unmutes a user from text channels.                        | !unmute [user]             |
| clear  | Deletes a specified amount of messages from text channel. | !clear [number (optional)] |

### Administrative

| Name | Description                   | Usage |
|------|-------------------------------|-------|
| setup | This command must be used for best functionality of the bot. Failure to do so will result in bugs. | !setup |
| setstatus | Changes the status message of the bot. | !setstatus [status] |

### Games

| Name | Description                   | Usage |
|------|-------------------------------|-------|
| flip | Flips a coin: heads or tails? | !flip |
| 8ball | Ask the magic 8-ball for an answer to a question. | !8ball [question] |

## Starting/Stopping the MySQL database

```
make start-mysql
make stop-mysql
```
# Astoria: A Discord Bot

A simple Discord bot built with discord.py v1.0+. Astoria currently is written
in Python 3.8.3

## Installation

```
pip install -r requirements.txt
python bot/bot.py
```

### Connecting to Discord

You'll need to create a `.env` file in the following format:

```
DISCORD_TOKEN=your_discord_token
DISCORD_GUILD=your_guild_name
CHANNEL_ID=your_channel_id
```

Then you'll need to install `python-dotenv` through pip.

### Connecting to the Database

Add to your `.env` file:

```
USERNAME=your_username
PASSWORD=your_password
DATABASE=name_of_your_database
HOST=how_you're_hosting_the_database
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

## Starting the MySQL database

This is more for me to remember.

```
sudo service mysql start
mysql -u root -p
sudo service mysql stop
```
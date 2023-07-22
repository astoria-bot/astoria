#!/bin/sh

usage() {
    echo "Usage: $Usage"
    exit 1
}

manpage() {
    cat << MANPAGE
NAME
        ${0##*/} - Create .env file containing Discord account information

SYNOPSIS $Usage

DESCRIPTION
    -c      Main channel ID where the bot posts messages
    -g      Discord guild value
    -t      Discord token value

MANPAGE

}

parseargs(){
    while getopts c:g:t:h OPTION; do
        case "$OPTION" in
            c) MAIN_CHANNEL_ID="$OPTARG";;
            g) DISCORD_GUILD="$OPTARG";;
            t) DISCORD_TOKEN="$OPTARG";;
            h) manpage; exit 0;;
        esac
    done
}

printvalues(){
    printf "Values:
    Main Channel ID: $MAIN_CHANNEL_ID
    Discord Guild: $DISCORD_GUILD
    Discord Token: $DISCORD_TOKEN\n"
}

envfilecreate(){
    echo "# This file is used to gather information needed to connect to a Discord server
CHANNEL_ID=$MAIN_CHANNEL_ID
DISCORD_GUILD=$DISCORD_GUILD
DISCORD_TOKEN=$DISCORD_TOKEN" > ./.env
}

parseargs "$@" || usage
printvalues

read -p "Are these the correct values? [y/n] " response
if [ "$response" != "y" ]; then
    exit
fi

envfilecreate
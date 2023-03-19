# Discord Hall of Fame Python Bot

A bot that allows messages with a certain emoji to be added to a list of messages that are displayed in a channel.

## Dependencies

- [discord.py](https://discordpy.readthedocs.io/en/stable/index.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. Clone the repository
2. Create a file called `.env` in the root directory
3. Install the dependencies with `pip3 install -r requirements.txt`
4. Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications)
5. Add the text permissions for your bot
6. Copy the Bot's Auth token
7. Add the token to the .env (see example.env)
8. Add the channel ID of the channel you want the bot to post in `bot.py`
9. Add the emoji ID of the emoji you want to use to add messages to the list in `bot.py`
10. Specify the number of reactions needed to copy the message to the HOF
11. Run the bot with `python3 main.py`
12. Bot will be alive as long as the server is up!

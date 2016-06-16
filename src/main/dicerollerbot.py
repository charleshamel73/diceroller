from slackbot.bot import Bot
from slackbot.bot import respond_to
import re

from src.main.Parser import Parser


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()

@respond_to('roll (.*)')
def parse(message,roll_string):
    Parser().parse(roll_string)
    message.reply('I can understand hi or HI!')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')
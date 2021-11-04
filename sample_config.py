import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1913653164:AAGP16l3WuKN85ukXpPsG4vFeS1v5ttxpRc")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "1383845"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0e3d2c299cc3c5cc26c283cecd2eb97c")

    # Authorized users to use this bot

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BQANOTEuMTA4LjU2LjEzMAG7oUh02qm9kF0zOj2uuN4sISSImtehHGN8lYsmE6JApGybRYoSUm3lrpniuqyoqnxZIk8b6flUUxRXXuIIlOfQwVOM0ShcoKPo0TZYE/vJJJJqF7SAlC9jtZSH0pTJUyihWG1o5KGP+dCjo5vIV81T6p2hKOqcNG+m2r88MCoCjshJ0+ouhKO6dwqXWute5uh4PNMMUmJUGkyl60TC2PL/Eiiw4eC2Ljna/Ebcylp2TCxtMiqCzV92Awfck6G6oYJzC8uiZvj5u8GNlblmKtx/9K9cke5QNTqq/NYZNxT1hOX4g/3tP66eph13HFVnvWbyQBw+K1O6T93Da48hzyFXEg==")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

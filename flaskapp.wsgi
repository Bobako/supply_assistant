#!/usr/bin/python3
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/FlaskApp/")

from supply_assistant import app as application
from supply_assistant import bot
bot.run()
application.secret_key = b'lol'

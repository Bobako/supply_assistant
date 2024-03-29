from threading import Thread
from telebot import TeleBot

from supply_assistant.cfg import config
from supply_assistant.models import Noti

bot = TeleBot(config["BOT"]["token"])


@bot.message_handler(commands=["id"])
def id_(message):
    bot.send_message(message.chat.id, str(message.chat.id))


class Bot:
    def __init__(self, session):
        self.session = session

    def run(self):
        print("bot is running")
        t = Thread(target=self.loop)
        t.start()

    def loop(self):
        while True:
            try:
                bot.polling(none_stop=True, interval=0)
            except Exception:
                pass

    def noti_admin(self, msg, tg_id):
        noti = self.session.query(Noti).one()
        if noti.send:
            try:
                bot.send_message(tg_id, msg)
            except Exception as e:
                print(type(e), e.args, "при отправке админу")
                return str(type(e)) + " " + str(e.args)
            else:
                return True

    def noti_vendor(self, id_, msg):
        try:
            bot.send_message(id_, msg)
        except Exception as e:
            print(type(e), e.args, "при отправке поставщику")
            return str(type(e)) + " " + str(e.args) + " " + str(e)
        else:
            return str(True)

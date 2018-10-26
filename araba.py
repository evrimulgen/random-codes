import sys
import time
import telepot
from telepot.loop import MessageLoop

"""
$ python2.7 skeleton.py <token>
A skeleton for your telepot programs.
"""

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)


TOKEN = "461288912:AAEa8DEl0-Din8sDp8fuVBUKiVtRsCG7Y9Q"  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)

# chat ('text', 'group', -254315048)
# deleteMessage(self, msg_identifier)

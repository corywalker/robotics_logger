import re

# Third-party
from oyoyo.client import IRCClient
from oyoyo.cmdhandler import DefaultCommandHandler
from oyoyo import helpers
import Pyro.core

# Initialize Oyoyo
HOST = 'irc.freenode.net'
PORT = 6667
NICK = 'ieeebot'
CHANNEL = '##utkieee'

class MyHandler(DefaultCommandHandler):
    def privmsg(self, nick, chan, msg):
        helpers.msg(self.client, chan, "Somebody privmsged me!!")

def connect_cb(cli):
    helpers.join(cli, CHANNEL)

cli = IRCClient(MyHandler, host=HOST, port=PORT, nick=NICK,
                connect_cb=connect_cb)
conn = cli.connect()

# Initialize Pyro
class SendMsg(Pyro.core.ObjBase):
        def __init__(self):
                Pyro.core.ObjBase.__init__(self)
        def send(self, message):
                helpers.msg(cli, CHANNEL, message)

Pyro.core.initServer()
daemon=Pyro.core.Daemon()
uri=daemon.connect(SendMsg(),"sendmsg")

print "The daemon runs on port:",daemon.port
print "The object's uri is:",uri

# Enter main loop
while True:
    conn.next()
    daemon.handleRequests()

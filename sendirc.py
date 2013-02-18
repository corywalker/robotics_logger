import sys
import Pyro.core

# you have to change the URI below to match your own host/port.
irc = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/sendmsg")

irc.send(sys.argv[1])

# irchandler.py
import logging
import logging.handlers
from datetime import datetime
# Third party
import Pyro.core
from django.core.management import setup_environ
from robotics_logger import settings
setup_environ(settings)
# Local
from storage.models import Message, Test

class RoboticsHandler(logging.Handler): # Inherit from logging.Handler
    def log(self, msg):
        elapsed = (datetime.now() - self.start).total_seconds()
        ts = "%06.2f" % elapsed
        if self.use_irc:
            self.irc.send("(%s) %s" % (ts, msg))
        m = Message()
        m.runtime = elapsed
        m.message = msg
        m.save()

    def __init__(self, use_irc):
        # run the regular Handler __init__
        logging.Handler.__init__(self)

        print use_irc
        self.use_irc = use_irc
        if self.use_irc:
            # you have to change the URI below to match your own host/port.
            self.irc = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/sendmsg")

        # timing info
        self.start = datetime.now()

        # send startup message
        from __main__ import __file__ as mainfn
        self.log("Starting %s..." % mainfn)
        self.test = Test()
        self.test.filename = mainfn
        self.test.start = self.start
        self.test.status = "AB"
        self.test.save()

    def emit(self, record):
        # record.message is the log message
        print "emitting %s" % record.message
        self.log(record.message)


def init_logger(use_irc=True):
    #LOG_FILENAME = "log.txt"
    
    # Create a logging object (after configuring logging)
    #logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logger = logging.getLogger()

    logging.handlers.RoboticsHandler = RoboticsHandler
    
    # create the handler object
    testHandler = logging.handlers.RoboticsHandler(use_irc)
    testHandler.setLevel(logging.INFO)
    
    # and finally we add the handler to the logging object
    logger.addHandler(testHandler)

    return logger

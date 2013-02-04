# smshandler.py
import logging

class IRCHandler(logging.Handler): # Inherit from logging.Handler
        def __init__(self):
                # run the regular Handler __init__
                logging.Handler.__init__(self)
        def emit(self, record):
                # record.message is the log message
                # sendsms.send(self.phonenumber, record.message)
                print record.message

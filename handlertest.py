# handlertest.py
import logging
#import logging.handlers
import irchandler

LOG_FILENAME = "log.txt"

# Create a logging object (after configuring logging)
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger()

# A little trickery because, at least for me, directly creating
# an SMSHandler object didn't work
logging.handlers.RoboticsHandler = irchandler.RoboticsHandler

# create the handler object
testHandler = logging.handlers.RoboticsHandler(True)
testHandler.setLevel(logging.INFO)

# and finally we add the handler to the logging object
logger.addHandler(testHandler)

#logger = irchandler.init_logger(True)

# And finally a test
while True:
    logger.info(raw_input())
    print "logged"

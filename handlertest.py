# handlertest.py
import logging
import logging.handlers
import irchandler

LOG_FILENAME = "log.txt"

# Create a logging object (after configuring logging)
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logger = logging.getLogger()

# A little trickery because, at least for me, directly creating
# an SMSHandler object didn't work
logging.handlers.IRCHandler = irchandler.IRCHandler

# create the handler object
testHandler = logging.handlers.IRCHandler()
# Configure the handler to only send SMS for critical errors
testHandler.setLevel(logging.DEBUG)

# and finally we add the handler to the logging object
logger.addHandler(testHandler)

# And finally a test
logger.debug('Test 1')
logger.info('Test 2')
logger.warning('Test 3')
logger.error('Test 4')
logger.critical('Test 5')

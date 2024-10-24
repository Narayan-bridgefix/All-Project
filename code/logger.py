import logging.config
import logging.handlers
from config import LOGGING_CONFIG, DEFAULT_LOGGER_NAME

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(DEFAULT_LOGGER_NAME)
smtp_handler = logging.handlers.SMTPHandler(mailhost='mailserver',
                            fromaddr='noreply@example.com',
                            toaddrs=['me@example.com'],
                            subject='Sample Log Mail',
                            credentials=('user','pwd'),
                            secure=None)
logger.addHandler(smtp_handler)
logger.info("logger configured")
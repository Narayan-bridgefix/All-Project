# import logging.config
# import logging.handlers
# from config import LOGGING_CONFIG, DEFAULT_LOGGER_NAME

# logging.config.dictConfig(LOGGING_CONFIG)
# logger = logging.getLogger(DEFAULT_LOGGER_NAME)
# smtp_handler = logging.handlers.SMTPHandler(mailhost='',
#                             fromaddr='narayanpunase11@gmail.com',
#                             toaddrs=['narayanpunase11@gmail.com'],
#                             subject='Sample Log Mail',
#                             credentials=('narayanpunase11@gmail.com','ftca emid esxi rrtv'),
#                             secure=None)
# # smtp_handler.emit('')
# logger.addHandler(smtp_handler)
# logger.info("logger configured")

# import logging
# import logging.handlers

# Create a custom formatter
# class CustomFormatter(logging.Formatter):
#     def format(self, record):
#         record.msg = f"[CUSTOM LOG] {record.msg}"  # Custom message format
#         return super().format(record)

# Configure the logger
# import logging
# log = logging.getLogger("mylogger")
# log.setLevel(logging.ERROR) 

# Create a formatter
# formatter = CustomFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configure the SMTP handler
# import pdb; pdb.set_trace()
# smtp_handler = logging.handlers.SMTPHandler(
#     mailhost=('smtp.gmail.com', 587),  # Replace with your SMTP server
#     fromaddr='narayanpunase11@gmail.com',  # Sender's email address
#     toaddrs=['narayanpunase11@gmail.com'],  # Recipient's email address
#     subject='The log',  # Subject of the email
#     credentials=('narayanpunase11@gmail.com', 'ftca emid esxi rrtv'),  # SMTP server credentials
#     secure=None  # Use None for no TLS, or provide a tuple for TLS
# )

# Set the level for the handler
# smtp_handler.setLevel(logging.DEBUG)  # Send emails for ERROR level and above
# smtp_handler.setFormatter(formatter)  # Attach the formatter to the handler

# Add the handler to the logger
# log.addHandler(smtp_handler)

# # Example log messages
# log.info("Did something")  # This will NOT send an email
# log.error("This is an error!")  # This WILL send an email
# log.critical("Critical issue occurred!")  # This WILL also send an email


# from django.conf import settings
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.SMTPHandler',
#             'mailhost': (settings.EMAIL_HOST, settings.EMAIL_PORT),
#             'fromaddr': settings.EMAIL_HOST_USER,
#             'toaddrs': ['narayanpunase11@gmail.com'],  # List of recipients
#             'subject': 'Error From Narayan Server',
#             'credentials': (settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD),
#             'secure': () if settings.EMAIL_USE_TLS else None,
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },

# }
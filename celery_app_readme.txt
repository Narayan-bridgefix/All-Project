For Celery Setup 

Start the WSL server 
-sudo service redis-server start
-redis-cli

now start the celery and celery beat server 
-celery -A managements worker --loglevel=info --pool=solo
-celery -A managements beat --loglevel=info

install celery and add in installed app
-celery


Configure the setting:-
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_IMPORTS = ('libmanagement.scheduled_task',)

if sending mail then also this-
from celery.schedules import crontab
# Celery beat settings
CELERY_BEAT_SCHEDULE = {
    'send-remainder-emails':{
        'task': 'libmanagement.scheduled_task.Send_mail_to_user',
        'schedule': crontab(hour=18, minute=40)
    },
}

#for sending email
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Use your email provider's SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'narayanpunase11@gmail.com'
EMAIL_HOST_PASSWORD = 'ftca emid esxi rrtv'
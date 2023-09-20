import os

from celery import Celery
from celery.schedules import crontab
from time import sleep
from datetime import timedelta
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'client.settings')

app = Celery('client')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

"""if you want give custom name to you 
    tasks user "@app.task(name="custom_name")"""

""" why "sleep"? this is only for demo that
 this function will take 10 second to run you don't want to do this in your
   actuall function"""

@app.task
def add(x,y):
    sleep(10)
    return x + y 

# Beat conf
# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
# Methode 2 if using this comment 'Beat conf'  from seetings.py  
# every 10 second od use timedelta

"""app.conf.beat_schedule = {
            'every-10-second': {
            'task': 'app.tasks.every_10_second',
            'schedule': 10,
            'args': ("why are you runnig", )
            }
                        }"""


# using timedelta

# app.conf.beat_schedule = {
#             'every-10-second': {
#             'task': 'app.tasks.every_10_second',
#             'schedule': timedelta(seconds=10),
#             'args': ("why are you runnig", )
#             }
#                         }
#  using crontab 


app.conf.beat_schedule = {
            'every-10-second': {
            'task': 'app.tasks.every_10_second',
            'schedule': crontab(minute='*/1'),
            'args': ("why are you runnig", )
            }
                        }
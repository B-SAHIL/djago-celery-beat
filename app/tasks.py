from celery import shared_task
import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from time import sleep


"""if you want give custom name to you 
    tasks user "@shared_task(name="custom_name")"""

""" why "sleep"? this is only for demo that
 this function will take 10 second to run you don't want to do this in your
   actuall function"""

@shared_task
def subs(x, y):
    sleep(10)
    return x - y

# this will run every 10 second "mentioned in setting.py "Beat conf""
@shared_task
def every_10_second(hey):
    print("why-are-you-runing")
    return hey


#These are just test fuction it dosn't clear any data
@shared_task
def creal_data(key):
    print("clearing data")
    return key

@shared_task
def clear_rabbitmq_data(key):
    print("Clear_RabbitMQ_Periodic from code")
    return key


# Create Schedule every 30 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)
# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='app.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(['hello']),  # Pass the arguments to the task as a JSON-encoded list
)
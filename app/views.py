from django.shortcuts import render
from client.celery import add
from celery.result import AsyncResult

# Local imports
from .tasks import subs

"""Keeping this here if you want to use these make
 sure to modifiy html files if you want to use these"""

"""Enqueue task using Delay()
def index(request):
    print("Result:")
    r1 = add.delay(10, 30)
    r2 = subs.delay(10, 30)
    print('result-',r1)
    print('resultr2-',r2)
    return render(request , 'home.html')

Enqueue task using apply_aysnc()
def index(request):
    print("Result:")
    r1 = add.apply_async(args=[10, 30])
    r2 = subs.apply_async(args=[10, 30])
    print('result-',r1)
    print('resultr2-',r2)
    return render(request , 'home.html')"""

# Home page or index
def index(request):
    result = add.delay(10,30)
    return render(request, 'home.html', {'result': result})


def check_result(request, task_id):
    result = AsyncResult(task_id)
    print('Ready', result.ready())
    print('succesfull', result.successful())
    print('failed', result.failed())
    return render(request, 'result.html', {'result': result})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
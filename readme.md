# Django templates are AI generated

# Django App Setup Guide

This guide will walk you through the process of setting up a Django app Celery, Celery Beat and creating schedule  task &  AsyncTask. 


## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- Python (3.x recommended)
- pip (Python package manager)
- Git (optional but recommended for version control)
- Redis server should be running

<!-- Make sure to change Port or other setting if using -->

## Installation

1. **Clone the Repository**

   ```shell
   git clone https://github.com/B-SAHIL/djago-celery-beat.git
   ```


2. **Start the Project**


```shell script
python -m venv venv
```

```shell script
venv\Scripts\activate 
```

<!-- on mac -->
```shell script
source venv/bin/activate
```

```shell script
pip install -r requirements.txt
```


```shell script
python manage.py migrate
```

<!-- Can create super user to check result from admin panel -->
<!-- JUST MAKE SURE TO DELETE THE RESULTS FROM ADMIN PANEL (Task results) AFTER SOMTIMES WHENEVER SERVER IS RUNNIG  -->

```shell script
python manage.py createsuperuser
```

- This will start app server

```shell script
python manage.py runserver
```

- This will start Celery worker server
```shell script
celery -A client worker -l info  
```
- This will start Celery Beat server
```shell script
celery -A client beat -l info 
```

<!-- All three server should be running at same time -->

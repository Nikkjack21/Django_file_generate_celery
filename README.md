
# Django Celery File Generate

This app focuses on generating files of random data
 using django and celery and redis.You could git clone this repository to get it working but I recommend following these manual steps so you 
understand what's required to get a basic idea of celery.



## Installation

Install virtual environment .

```bash
 pip install virtualenv

```
Create a virtual environment .

```bash
 virtualenv myenv
 
```

Create the requirements.txt file to install the packages required: .

```bash
django
redis
celery
 
```


Activate your virtual environment and install the requirements in the requirements.txt file:

```bash
pip install -r requirements.txt
 
```


Create your Django project:

```bash
django-admin startproject new_project . 

```

Open the settings.py file and add some basic Celery configuration - ensure these are prefixed with CELERY_:
```bash
# Celery - prefix with CELERY_
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True
```



Add a celery.py file to the project directory, i.e. new_project:
```bash


from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_project.settings")

app = Celery("celery_project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

```

Ensure the celery app gets loaded when the Django project starts by adding the following to new_project > __init__.py
```bash
from __future__ import absolute_import, unicode_literals

from .celery import app as celery_app

__all__ = ("celery_app",)


```

# Follow celery docs for to know how to start celery worker.
The above are neccessary steps needed, Now install redis

```bash
pip install reddis. 

```

Now open two terminals, In one terminal start redis server and next one use ping and recieve pong to ensure everything working fne.

```bash
redis-server
redis-cli ping
```

# That's all. Now create celery tasks and run.
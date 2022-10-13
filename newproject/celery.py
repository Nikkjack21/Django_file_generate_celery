from __future__ import unicode_literals, absolute_import
import os

from celery import Celery
from django.conf import settings
from celery.signals import setup_logging


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newproject.settings")
app = Celery("newproject")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()








@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.reqquest!r}")

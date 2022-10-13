from celery import shared_task
from django.views import View
from faker import Faker
import csv
from django_celery_results.models import TaskResult
import os
from pathlib import Path
import shutil


@shared_task(bind=True)
def generate_file(self, n):
    output = "turbolab.csv"
    coloumns = ["Task ID", "Status", "Results"]
    fake = Faker()
    with open(output, "w") as file:
        writer = csv.writer(file)
        tasks = TaskResult.objects.all()
        for tk in range(n):
            tk = fake.name()
            writer.writerow([tk])
    Path("data").mkdir(exist_ok=True)
    for file in os.listdir():
        if file == "turbolab.csv":
            shutil.copy(file, "data")
    return True

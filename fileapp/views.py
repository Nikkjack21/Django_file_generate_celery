from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from time import sleep
import os
from fileapp.tasks import generate_file

# Create your views here.



def new_file(request):
    if request.method=='POST':
        n=int(request.POST.get('num'))
        print(n)
        generate_file.delay(n)
    return render(request, 'index.html')

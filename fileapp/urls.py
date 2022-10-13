from django.urls import path

from .import views

urlpatterns=[
    path('',views.new_file,name='new'),
]
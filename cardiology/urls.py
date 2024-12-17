from cardiology.views import *
from django.urls import path
urlpatterns=[
    path('cardio/',cardio,name='cardio'),
    path('admin/',admin,name='admin'),
]
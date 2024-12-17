from neurology.views import *
from django.urls import path
urlpatterns=[
    path('neuro/',neuro,name='neuro'),
    path('medical/',medical,name='medical'),
]
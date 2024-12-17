from django.shortcuts import render

# Create your views here.
def neuro(request):
    return render (request,'neuro.html')
def medical (request):
    return render (request,'medical.html')
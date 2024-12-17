from django.shortcuts import render

# Create your views here.
def cardio (request):
    return render (request,'cardio.html')
def admin (request):
    return render (request,'admin.html')
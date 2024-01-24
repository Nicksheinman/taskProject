from django.shortcuts import render, HttpResponse
from datetime import date, timedelta
from random import choices
from .models import Task, User

# Create your views here.

def home(request):
    return render(template_name='index.html', request=request,context={"tasks":Task.objects.all()})

def create_task(request):
    for a in range(30):
        name='adsad'
        explain='dasd'
        status='incomplete'
        datee='dadsad'
        Task(name=name, explain=explain, status=status,date=datee).save()
    return HttpResponse("tasks created")
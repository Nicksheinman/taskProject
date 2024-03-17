from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from random import choices
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import *
from faker import *
# Create your views here.

def home(request):
    return render(template_name='index.html', request=request,context={"tasks":Task.objects.all()})

def create_task(request):
    for a in range(30):
        name='adsad'
        explain='dasd'
        status=False
        datee='27/11/2024'
        Task(name=name, explain=explain, status=status,date=datee).save()
    return HttpResponse("tasks created")
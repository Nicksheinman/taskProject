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
    form=AddTask()
    return render(template_name='index.html', request=request,context={"form":form,"tasks":Task.objects.all()})

def create_task(request):
    for a in range(30):
        name='adsad'
        explain='dasd'
        status=False
        datee='27/11/2024'
        Task(name=name, explain=explain, status=status,date=datee).save()
    return HttpResponse("tasks created")

def register(request):
    form= Create_user_f()
    if request.method== "POST":
        form=Create_user_f(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request=request, template_name='register.html', context={"form":form})

def login(request):
    form=LoginForm()
    if request.method== "POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username= request.POST.get("username")
            password= request.POST.get("password")
            user=authenticate(request=request, username=username, password=password)
            if user is not None:
                auth.login(request=request, user=user)
                return redirect('/')
    return render(request=request,template_name='login.html', context={'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login/')
def dashboard(request):
    return render(request=request, template_name='dashboard.html',context={"form":AddTask(),"tasks":Task.objects.all()})

@login_required(login_url='login/')
def create(request):
    if request.method == "POST":
        Task(request.POST).save()
        return HttpResponseRedirect("dashboard")
    return render(request=request, template_name='create.html',context={"form":AddTask(),"tasks":Task.objects.all()} )

@login_required(login_url='login/')
def read(request,pk):
    task=Task.objects.get(id=pk)
    return render(request=request, template_name='readTask.Html', context={'form':task})

@login_required(login_url='login/')
def update(request, pk):
    task= Task.objects.get(id=pk)
    tform= UpdateForm(instance=task)
    if request.method == "POST":
        tform=UpdateForm(request.POST,instance=task)
        if tform.is_valid():
            tform.save()
            return redirect("dashboard")
    return render(request=request, template_name='update.html', context={'form':tform})

def deleteT(request, pk):
    task= Task.objects.get(id=pk)
    if request.method == 'GET':
        task.delete()
        return redirect('dashboard')
    return redirect('dashboard')
from django.shortcuts import render, redirect
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import forms
from .models import *
from .forms import TaskForm, CreateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    tset = Task.objects.all()
    total_tasks = Task.objects.all().count()
    pending = Task.objects.filter(status='Pending').count()
    completed = Task.objects.filter(status='Completed').count()
    context = {'tset': tset, 'total_tasks': total_tasks, 'pending': pending, 'completed': completed}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def AllTask(request):
    tallset = Task.objects.all()
    return render(request, 'alltasks.html', {'tallset': tallset})


@login_required(login_url='login')
def CreateTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    # else:
    #     form = TaskForm()
    context = {'form': form}
    return render(request, 'create.html', context)


def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def Search(request):
    query = request.GET.get('search')
    stask = Task.objects.filter(status__icontains=query)
    params = {'stask': stask}
    return render(request, 'search.html', params)

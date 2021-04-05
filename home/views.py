from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from accounts.models import *
from .forms import CreatePost
from .decorators import *
from accounts.forms import *
# Create your views here.


def home(request):
    post = Posts.objects.all()
    return render(request, 'home/home.html', {'post': post})


def Post(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'home/post.html', {'post': post})


@allowed_users(allowed_roles=['teacher', 'admin'])
def Create(request):
    form = CreatePost()
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'home/create.html', context)


@allowed_users(allowed_roles=['teacher', 'admin'])
def Update(request, pk):
    post = Posts.objects.get(id=pk)
    form = CreatePost(instance=post)
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CreatePost(instance=post)
    context = {'form': form}
    return render(request, 'home/create.html', context)


@allowed_users(allowed_roles=['teacher', 'admin'])
def Delete(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    context = {'item': post}
    return render(request, 'home/delete.html', context)

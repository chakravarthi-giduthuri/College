from django.contrib.auth.models import Group
from django.http import HttpResponse
from .models import *
from .forms import StudentRegisterForm, TeacherRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def register(request):
    return render(request, 'accounts/register.html')


def studentRegister(request):
    next = request.GET.get('next')
    form = StudentRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        # year = form.cleaned_data.get('year')
        user.is_student = True
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='student')
        user.groups.add(group)
        student = Student.objects.create(user=user)
        # student.year = form.cleaned_data.get('year')
        student.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'accounts/registerform.html', {'form': form})


def teacherRegister(request):
    next = request.GET.get('next')
    form = TeacherRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        # year = form.cleaned_data.get('year')
        user.is_teacher = True
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='teacher')
        user.groups.add(group)
        teacher = Teacher.objects.create(user=user)
        # student.year = form.cleaned_data.get('year')
        teacher.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'accounts/registerform.html', {'form': form})


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username OR password is not correct')
            return render(request, 'accounts/login.html')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

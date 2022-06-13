from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from mainapp.views import *

from authapp.forms import LoginForm, RegisterForm



def login(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('base'))
    else:
        form = LoginForm()
    content = {
        'title': 'Авторизация',
        'form': form,
        'categories': categories,
    }
    return render(request, 'authapp/login.html', content)


def register(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = RegisterForm()
    content = {
        'title': 'Регистрация',
        'form': form,
        'categories': categories,
    }
    return render(request, 'authapp/register.html', content)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('base'))

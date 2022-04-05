from click import pass_context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlesForm

# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'empty111'

    usrpas = Articles.objects.all()
    form = ArticlesForm()
    data = {
        'title': 'Login Page',
        'usrpas': usrpas,
        'form': form,
        'error': error 
    }
    return render(request, 'login/login.html', data)


def registration(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'empty!!!'

    usrpas = Articles.objects.all()
    form = ArticlesForm()
    data = {
        'title': 'Registration',
        'form': form,
        'error': error 
    }
    return render(request, 'login/registration.html', data)
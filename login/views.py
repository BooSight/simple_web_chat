from click import pass_context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Articles
from .forms import ArticlesForm

# Create your views here.


def index(request):
    error = ''
    if request.method == 'POST':
        usr = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            obj = Articles.objects.get(username=usr)
            obj2 = obj.password
            if str(usr) == str(obj):
                if str(pswd) == str(obj2):
                    return redirect('/public_chat')
                else:
                    error = 'Incorrect Password'
        except:
            error = 'Incorrect Username'

    form = ArticlesForm()
    data = {
        'title': 'Login Page',
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
            return redirect('/public_chat')
        else:
            error = 'This Username is busy'

    form = ArticlesForm()
    data = {
        'title': 'Registration',
        'form': form,
        'error': error
    }
    return render(request, 'login/registration.html', data)


def public_chat(request):
    data = {
        'title': 'Public Chat'
    }
    return render(request, 'login/public_chat.html', data)

# from click import pass_context
from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpRequest
# from requests import post
# from .models import Articles
from .forms import ArticlesForm, Pub_chat_Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def index(request):
    # error = ''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/public_chat')
        # usr = request.POST.get('username')
        # pswd = request.POST.get('password')
        # try:
        #     obj = Articles.objects.get(username=usr)
        #     obj2 = obj.password
        #     if str(usr) == str(obj):
        #         if str(pswd) == str(obj2):
        #             return redirect('/public_chat')
        #         else:
        #             error = 'Incorrect Password'
        # except:
        #     error = 'Incorrect Username'
    else:
        form = AuthenticationForm()
    # form = ArticlesForm()
    data = {
        'title': 'Login Page',
        'form': form
        # 'error': error
    }
    return render(request, 'login/login.html', data)


def registration(request):
    # error = ''
    if request.method == 'POST':
        # form = ArticlesForm(request.POST)
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/public_chat')
        

    # form = ArticlesForm()
    else:
        form = UserCreationForm()
    data = {
        'title': 'Registration',
        'form': form
        # 'error': error
    }
    return render(request, 'login/registration.html', data)


def logout_views(request):
    if request.method == 'POST':
        
        logout(request)
        return redirect('login')


def public_chat(request):
    form = Pub_chat_Form()
    data = {
        'title': 'Public Chat',
        'form': form
    }
    return render(request, 'login/public_chat.html', data)

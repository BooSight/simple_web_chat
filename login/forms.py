from pyexpat import model
from attr import fields
from matplotlib import widgets
from .models import Articles, Pub_chat
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, DateTimeField


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['username', 'password', 'mail']

        widgets = {
            "username": TextInput({
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "password": PasswordInput({
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "mail": EmailInput({
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Mail'
            })
        }


class Pub_chat_Form(ModelForm):
    class Meta:
        model = Pub_chat
        fields = ['text_area']

        widgets = {
            "user_name": TextInput({
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "text_area": TextInput({
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Text'
            }),
            "msg_date": TextInput({
                'type': 'datetime',
                'class': 'form-control'
            }),
        }



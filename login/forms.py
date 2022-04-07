from matplotlib import widgets
from .models import Articles
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


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

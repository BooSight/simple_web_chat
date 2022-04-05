from matplotlib import widgets
from .models import Articles
from django.forms import ModelForm, TextInput, PasswordInput


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
            "mail": TextInput({
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Mail'
            })
        }

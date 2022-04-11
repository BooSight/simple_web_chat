from tabnanny import verbose
from django import forms
from django.db import models

# Create your models here.
class Articles(models.Model):
    username = models.CharField('Username', max_length=20, unique=True)
    password = models.CharField('Password', max_length=20)
    mail = models.CharField('Mail', max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    

class Pub_chat(models.Model):
    user_name = models.CharField('username', max_length=20)
    text_area = models.TextField('input_txt') 
    msg_date = models.DateTimeField('date')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Pub_chat'
        verbose_name_plural = 'Pub_chats'

    
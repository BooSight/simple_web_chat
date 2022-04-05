from tabnanny import verbose
from django.db import models

# Create your models here.
class Articles(models.Model):
    username = models.CharField('Username', max_length=20)
    password = models.CharField('Password', max_length=20)
    mail = models.CharField('Mail', max_length=20)

    # def __str__(self):
        # return self.title
    
    

    
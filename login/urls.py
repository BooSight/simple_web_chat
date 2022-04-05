from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('registration', views.registration, name='registration')
]
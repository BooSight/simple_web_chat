from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('registration', views.registration, name='registration'),
    path('logout_views', views.logout_views, name='logout'),
    path('public_chat', views.public_chat, name='public_chat'),
    path('public_chat_read', views.public_chat_read, name='public_chat_read'),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('event', views.event, name='event'),
]
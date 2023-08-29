from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('event', views.event, name='event'),
    path('education', views.education, name='education'),
    path('publications', views.publications, name='publications'),
    path('galleries', views.galleries, name='galleries')
]
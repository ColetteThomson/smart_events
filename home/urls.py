from django.urls import path
from . import views

urlpatterns = [
    # blank path to indicate default as home page
    path('', views.welcome, name='home'),
]

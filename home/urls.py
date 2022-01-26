from django.urls import path
from . import views

urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()' CHANGE CLASS NAME!! (POSTLIST)
    path('', views.welcome, name='home'),
]
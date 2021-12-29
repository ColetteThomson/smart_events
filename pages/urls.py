from . import views
from django.urls import path

urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()'
    path('', views.PostList.as_view(), name='home')
]
from django.urls import path
from . import views

# urls paths for 'PostList' and 'PostDetail'
urlpatterns = [
    # blank path to indicate default as home page
    # and render this class as a view using 'as_view()'
    path('', views.PostList.as_view(), name='post_list'),
    # 'slug' keyword matches 'slug' parameter in get method of PostDetail class
    # path converter (slug) if matched to return a string, if not a 404 message
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # number of likes using slug (from post_detail.html)
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]

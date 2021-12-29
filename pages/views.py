from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    # filter contents of post table by '1' (published) ordered by descending date
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # to render html view
    template_name = 'index.html'
    # number of posts that appear on front page
    paginate_by = 6

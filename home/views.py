# 'reverse' s/cut allows lookup of a url by name given in urls.py
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
# 'httpResponseRedirect' allows reloading of a template (post_detail)
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

# # NEED TO CHANGE CLASS NAME!!!
# class PostList(generic.ListView):
#     model = Post
#     # filter contents of post table by '1' (published) by descending date
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     # to render html view
#     template_name = 'index.html'

#     # number of posts that appear on front page
#     paginate_by = 6

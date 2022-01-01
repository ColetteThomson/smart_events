from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class PostList(generic.ListView):
    model = Post
    # filter contents of post table by '1' (published) by descending date
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # to render html view
    template_name = 'index.html'
    # number of posts that appear on front page
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # filter for active posts
        queryset = Post.objects.filter(status=1)
        # use unique slug to get published post
        post = get_object_or_404(queryset, slug=slug)
        # get post's approved comments in descending date order
        comments = post.comments.filter(approved=True).order_by('-created_on')
        # determine if logged-in user has liked post or not
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # combine template with context dict to return post with liked comments
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )

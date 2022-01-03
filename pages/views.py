from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


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
                # to tell user their comment is awaiting approval
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
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
     
        # obtain all data posted from form
        comment_form = CommentForm(data=request.POST)

        # if comment form is valid (all fields completed)
        if comment_form.is_valid():
            # obtain email and name from logged in user details
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # call save method on form
            comment = comment_form.save(commit=False)
            # then determine for which post a comment has been left
            comment.post = post
            # then save the comment
            comment.save()
        # if comment form not valid return empty form
        else:
            comment_form = CommentForm()

        # combine template with context dict to return post with liked comments
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

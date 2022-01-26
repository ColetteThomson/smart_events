from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# tuple showing status of post
STATUS = ((0, "Draft"), (1, "Published"))


# ERD model for class Post
class Post(models.Model):

    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # if one-to-many author relationship is deleted so will all related records
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()
    blog_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # helper methods for class Post:
    # order posts based on created_on field (in descending order)
    class Meta:
        ordering = ['-created_on']

    # returns a string representation of an object
    def __str__(self):
        return self.blog_title

    # returns total number of likes on a post
    def number_of_likes(self):
        return self.likes.count()


# ERD model for class Comment
class Comment(models.Model):
    # if one-to-many author relationship is deleted so will all related records
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # helper methods for class Comment:
    # order posts based on created_on field (in ascending order)
    class Meta:
        ordering = ['created_on']

    # returns a string representation of an object
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# decorator to register both post model & post admin class for admin site
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # summernote to be applied to 'content' field
    summernote_fields = ('blog_content')

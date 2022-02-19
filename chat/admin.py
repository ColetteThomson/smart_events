from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ register decorator: post model; post admin classes for admin panel """
    # customise list view of admin panel
    list_display = ('blog_title', 'slug', 'status', 'created_on')
    # add search fields for either title or content
    search_fields = ['blog_title', 'blog_content']
    # prepopulate slug field when completing title field
    prepopulated_fields = {'slug': ('blog_title',)}
    # add filter for post status and created_by date
    list_filter = ('status', 'created_on')
    # summernote formatting to be applied to 'content' field
    summernote_fields = ('blog_content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ register decorator: comment class for admin panel """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # add an approved comments section
    actions = ['approve_comments']

    # set boolean field to True (to approve comment)
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

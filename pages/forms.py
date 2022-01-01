from .models import Comment
from django import forms

# CommentForm class to inherit from the base form
class CommentForm(forms.ModelForm):
    # shows which model to use and what fields to display
    class Meta:
        model = Comment
        fields = ('body',)

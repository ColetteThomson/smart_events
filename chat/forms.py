from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """ CommentForm class to inherit from the base form """
    # shows which model to use and what fields to display
    class Meta:
        model = Comment
        fields = ('body',)

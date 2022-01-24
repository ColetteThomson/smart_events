from django import forms
from django.forms import ModelForm
from .models import People, Project
from datetime import date

# people choices
# PEOPLE_CHOICES = []

# create an project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields to be imported from class Project
        fields = ('project_name', 'project_date', 'people', 'project_manager', 'description')
        # set the label to none
        labels = {
            'project_name': '',
            'project_date': 'YYYY-MM-DD',
            #'job_title': 'job title',
            'people': 'people',
            'project_manager': 'Project Manager',
            'description': '',
        }
        
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            
            #'project_date': forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Project Date'}),

            'people': forms.Select(attrs={'class': 'form-select', 'placeholder': 'People'}),
            #'job_title': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Job Title'}),
            'project_manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Project Manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


# create a people form
class PeopleForm(ModelForm):
    class Meta:
        model = People
        # fields to be imported from class People
        fields = ('person_name', 'job_title', 'contact_no', 'person_email')
        labels = {
            'person_name': '',
            'job_title': '',
            'contact_no': '',
            'person_email': '',
        }
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Person Name'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Person Email'}),
        }

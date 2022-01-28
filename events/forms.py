from django import forms
from django.forms import ModelForm
from .models import PeopleAdmin, Project, PeopleTechSupport
from datetime import date


# create a people form
class AdminForm(ModelForm):
    class Meta:
        model = PeopleAdmin
        # fields to be imported from class People
        fields = ('person_name', 'contact_no', 'person_email')
        labels = {
            'person_name': 'Person Name',
            'contact_no': 'Person Contact Number',
            'person_email': 'Person Email',
            #'ad_owner': 'People Manager',
        }
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control'}),
            #'ad_owner': forms.Select(attrs={'class': 'form-select'}),
        }


# create a 'Resource: Tech Support' form
class TechSupportForm(ModelForm):
    class Meta:
        model = PeopleTechSupport
        # fields to be imported from class PeopleTechSupport
        fields = ('person_name_tech', 'contact_no_tech', 'person_email_tech')
        labels = {
            'person_name_tech': 'Person Name',
            'contact_no_tech': 'Person Contact Number',
            'person_email_tech': 'Person Email',
            #'ts_owner': 'People Manager'
        }
        widgets = {
            'person_name_tech': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no_tech': forms.TextInput(attrs={'class': 'form-control'}),
            'person_email_tech': forms.EmailInput(attrs={'class': 'form-control'}),
            #'ts_owner': forms.Select(attrs={'class': 'form-select'}),
        }


# create (add) a project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #
        ##exclude = ['project_manager']
        # fields to be imported from class Project
        fields = ('project_name', 'project_date', 'resource_admin', 'resource_tech', 'project_manager', 'description')
        # set the label to none
        labels = {
            'project_name': 'Project Name',
            'project_date': 'YYYY-MM-DD',
            'resource_admin': 'Resource: Project Administration',
            'resource_tech': 'Resource: Tech Support',
            'project_manager': 'Project Manager',
            'description': 'Project Description',
        }
        
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            
            #'project_date': forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Project Date'}),

            'resource_admin': forms.Select(attrs={'class': 'form-select'}),
            'resource_tech': forms.Select(attrs={'class': 'form-select'}),
            'project_manager': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

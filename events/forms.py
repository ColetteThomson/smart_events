from django import forms
from django.forms import ModelForm
from .models import PeopleAdministration, Project, PeopleTechSupport
from datetime import date


# create a administration people form
class AdminForm(ModelForm):
    class Meta:
        model = PeopleAdministration
        # fields to be imported from class PeopleAdministration
        fields = ('person_name', 'contact_no', 'person_email', 'project_experience', 'ad_owner')
        labels = {
            'person_name': 'Person Name',
            'contact_no': 'Person Contact Number',
            'person_email': 'Person Email',
            'project experience': 'Project Experience',
            'ad_owner': 'People Manager',
        }
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'project_experience': forms.Textarea(attrs={'class': 'form-control'}),
            'ad_owner': forms.TextInput(attrs={'class': 'form-control'}),
        }


# create a 'Resource: Tech Support' form
class TechSupportForm(ModelForm):
    class Meta:
        model = PeopleTechSupport
        # fields to be imported from class PeopleTechSupport
        fields = ('person_name_tech', 'contact_no_tech', 'person_email_tech', 'project_experience', 'ts_owner')
        labels = {
            'person_name_tech': 'Person Name',
            'contact_no_tech': 'Person Contact Number',
            'person_email_tech': 'Person Email',
            'project_experience': 'Project Experience',
            'ts_owner': 'People Manager',
        }
        widgets = {
            'person_name_tech': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no_tech': forms.TextInput(attrs={'class': 'form-control'}),
            'person_email_tech': forms.EmailInput(attrs={'class': 'form-control'}),
            'project_experience': forms.Textarea(attrs={'class': 'form-control'}),
            'ts_owner': forms.TextInput(attrs={'class': 'form-control'}),
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
            'project_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

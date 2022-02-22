from django import forms
from django.forms import ModelForm
from .models import PeopleAdministration, Project, PeopleTechSupport


class AdminForm(ModelForm):
    """ create (add) administration people form """
    # form fields
    class Meta:
        model = PeopleAdministration
        # fields to be imported from class PeopleAdministration
        fields = ('person_name', 'contact_no', 'person_email',
                  'project_experience', 'ad_owner')
        # labels for form fields
        labels = {
            'person_name': 'Person Name',
            'contact_no': 'Person Contact Number',
            'person_email': 'Person Email',
            'project experience': 'Project Experience',
            'ad_owner': 'Admin People Manager',
        }
        # render html form input elements
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'project_experience': forms.Textarea(attrs={
                'class': 'form-control'}),
            'ad_owner': forms.TextInput(attrs={'class': 'form-control',
                                               'id': 'user',
                                               'type': 'hidden'}),
        }


class TechSupportForm(ModelForm):
    """ create (add) Tech Support form """
    # form fields
    class Meta:
        model = PeopleTechSupport
        # fields to be imported from class PeopleTechSupport
        fields = ('person_name_tech', 'contact_no_tech', 'person_email_tech',
                  'project_experience', 'ts_owner')
        # labels for form fields
        labels = {
            'person_name_tech': 'Person Name',
            'contact_no_tech': 'Person Contact Number',
            'person_email_tech': 'Person Email',
            'project_experience': 'Project Experience',
            'ts_owner': 'Tech Support People Manager',
        }
        # render html form input elements
        widgets = {
            'person_name_tech': forms.TextInput(attrs={'class':
                                                       'form-control'}),
            'contact_no_tech': forms.TextInput(attrs={'class':
                                                      'form-control'}),
            'person_email_tech': forms.EmailInput(attrs={'class':
                                                         'form-control'}),
            'project_experience': forms.Textarea(attrs={'class':
                                                        'form-control'}),
            'ts_owner': forms.TextInput(attrs={'class': 'form-control',
                                               'id': 'user',
                                               'type': 'hidden'}),
        }


class ProjectForm(ModelForm):
    """ create (add) a project form """
    # form fields
    class Meta:
        model = Project
        # fields to be imported from class Project
        fields = ('project_name', 'project_date', 'resource_admin',
                  'resource_tech', 'description', 'project_manager')
        # labels for form fields
        labels = {
            'project_name': 'Project Name',
            'project_date': 'Date and Time (YYYY-MM-DD) (HH:MM:SS)',
            'resource_admin': 'Resource - Project Admin',
            'resource_tech': 'Resource - Technical Analyst',
            'description': 'Project Description',
            'project_manager': 'Project Manager',
        }
        # render html form input elements
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'resource_admin': forms.Select(attrs={'class': 'form-select'}),
            'resource_tech': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_manager': forms.TextInput(attrs={'class': 'form-control',
                                                      'id': 'user',
                                                      'type': 'hidden'}),
        }

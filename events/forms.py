from django import forms
from django.forms import ModelForm
from .models import PeopleAdministration, Project, PeopleTechSupport


# create a administration people form
class AdminForm(ModelForm):
    """ form fields """
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
                                        'value': '', 'id': 'user',
                                               'type': 'hidden'}),
        }


# create a 'Resource: Tech Support' form
class TechSupportForm(ModelForm):
    """ form fields """
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
                                               'value': '', 'id': 'user',
                                               'type': 'hidden'}),
        }


# create (add) a project form
class ProjectForm(ModelForm):
    """ form fields """
    class Meta:
        model = Project
        # fields to be imported from class Project
        fields = ('project_name', 'project_date', 'resource_admin',
                  'resource_tech', 'project_manager', 'description')
        # labels for form fields
        labels = {
            'project_name': 'Project Name',
            'project_date': 'Date (YYYY-MM-DD) and Time (HH-MM-SS)',
            'resource_admin': 'Resource: Project Administration',
            'resource_tech': 'Resource: Tech Support',
            'project_manager': 'Project Manager',
            'description': 'Project Description',
        }
        # render html form input elements
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'resource_admin': forms.Select(attrs={'class': 'form-select'}),
            'resource_tech': forms.Select(attrs={'class': 'form-select'}),
            'project_manager': forms.TextInput(attrs={'class': 'form-control',
                                                      'value': '',
                                                      'id': 'user',
                                                      'type': 'hidden'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

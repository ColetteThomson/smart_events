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
            'person_name': '',
            'contact_no': '',
            'person_email': '',
        }
        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Person Name'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Person Email'}),
        }


# create a 'Resource: Tech Support' form
class TechSupportForm(ModelForm):
    class Meta:
        model = PeopleTechSupport
        # fields to be imported from class PeopleTechSupport
        fields = ('person_name_tech', 'contact_no_tech', 'person_email_tech')
        labels = {
            'person_name_tech': '',
            'contact_no_tech': '',
            'person_email_tech': '',
        }
        widgets = {
            'person_name_tech': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Person Name'}),
            'contact_no_tech': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'person_email_tech': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Person Email'}),
        }


# create (add) a project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields to be imported from class Project
        fields = ('project_name', 'project_date', 'resource_admin', 'resource_tech', 'project_manager', 'description')
        # set the label to none
        labels = {
            'project_name': '',
            'project_date': 'YYYY-MM-DD',
            'resource_admin': '',
            'resource_tech': '',
            'project_manager': '',
            'description': '',
        }
        
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            
            #'project_date': forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Project Date'}),

            'resource_admin': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Resource: Project Admin'}),
            'resource_tech': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Resource: Tech Support'}),
            'project_manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Project Manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Project Description'}),
        }






# JobTitle = (
#     ("Technical Analyst", "Technical Analyst"),
#     ("Project_Admin", "Project Admin"),
#     ("UX_Design", "UX Design"),
#     ("Business_Analyst", "Business Analyst")
# )

# class PeopleInfoForm(ModelForm):
#     class Meta:
#         model = People
#         # fields to be imported from class People
#         fields = ('person_name', 'job_title','contact_no', 'person_email')
#         labels = {
#             'person_name': '',
#             'job_title': '',
#             'contact_no': '',
#             'person_email': '',
#         }
#         widgets = {
#             'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Person Name'}),
#             'job_title': forms.ChoiceField(choices = JobTitle, 'class': 'form-control', 'placeholder': 'Job Title'),
#             'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
#             'person_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Person Email'}),
#         }

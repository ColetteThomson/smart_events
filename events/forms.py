from django import forms
from django.forms import ModelForm
from .models import People, Project, TechSupport
from datetime import date

# create (add) a project form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields to be imported from class Project
        fields = ('project_name', 'project_date', 'people', 'resource_TS','project_manager', 'description')
        # set the label to none
        labels = {
            'project_name': '',
            'project_date': 'YYYY-MM-DD',
            #'job_title': 'job title',
            'people': 'Resource: Project Admin',
            'resource_TS': 'Resource: Tech Support',
            'project_manager': 'Project Manager',
            'description': '',
        }
        
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            
            #'project_date': forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Project Date'}),

            'people': forms.Select(attrs={'class': 'form-select', 'placeholder': 'People'}),
            'resource_TS': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Resource: Tech Support'}),

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


# create a 'Resource: Tech Support' form
class TechSupportForm(ModelForm):
    class Meta:
        model = TechSupport
        # fields to be imported from class TechSupport
        fields = ('person_name_TS', 'contact_no', 'person_email')
        labels = {
            'person_name_TS': '',
            'contact_no': '',
            'person_email': '',
        }
        widgets = {
            'person_name_TS': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Person Name'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Person Email'}),
        }




JobTitle = (
    ("Tech_Support", "Tech Support"),
    ("Project_Admin", "Project Admin"),
    ("UX_Design", "UX Design"),
)

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

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, PeopleAdministration, PeopleTechSupport


@admin.register(PeopleAdministration)
class PeopleAdministrationAdmin(admin.ModelAdmin):
    """ decorator to register PeopleAdmin admin class for admin site """
    # customise list view of admin panel
    list_display = ('person_name', 'contact_no', 'person_email')
    # order people alphabetically (ascending)
    ordering = ('person_name',)
    # add search fields for person name
    search_fields = ['person_name']


@admin.register(PeopleTechSupport)
class PeopleTechSupportAdmin(admin.ModelAdmin):
    """ decorator to register TechSupport admin class for admin site """
    # customise list view of admin panel
    list_display = ('person_name_tech', 'contact_no_tech', 'person_email_tech')
    # order people alphabetically (ascending)
    ordering = ('person_name_tech',)
    # add search fields for person name
    search_fields = ['person_name_tech']


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    """ decorator to register Project admin class for admin site """
    # customise list view of admin panel
    list_display = ('project_name', 'project_date')
    # order projects alphabetically
    ordering = ('project_name',)
    # add search fields for either project or date
    search_fields = ['project_name', 'project_date']
    # add filter for project name and date
    list_filter = ('project_name', 'project_date')
    # summernote formatting to be applied to project's 'description' field
    summernote_fields = ('description')

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, People, SiteUser


# decorator to register People admin class for admin site
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    # customise list view of admin panel
    list_display = ('person_name', 'job_title', 'contact_no', 'person_email')
    # order people alphabetically (ascending)
    ordering = ('person_name',)
    # add search fields for person name
    search_fields = ['person_name']


# decorator to register User admin class for admin site
@admin.register(SiteUser)
class UsersAdmin(admin.ModelAdmin):
    # customise list view of admin panel
    list_display = ('first_name', 'last_name', 'user_email')
    # order users alphabetically by last name
    ordering = ('last_name',)
    # add search fields for either user's last name or email
    search_fields = ['last_name', 'user_email']
    # add filter for user's last name or email
    list_filter = ('last_name', 'user_email')


# decorator to register Project admin class for admin site
@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    # customise list view of admin panel
    list_display = ('project_name', 'project_date', 'project_manager')
    # order projects alphabetically
    ordering = ('project_name',)
    # add search fields for either project or date or manager
    search_fields = ['project_name', 'project_date', 'project_manager']
    # add filter for project date and manager
    list_filter = ('project_name', 'project_date')
    # summernote formatting to be applied to project's 'description' field
    summernote_fields = ('description')

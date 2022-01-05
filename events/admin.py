from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


# decorator to register both post model & post admin class for admin site
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    # customise list view of admin panel
    list_display = ('event_name', 'venue', 'event_date', 'manager')
    # add search fields for either event or date
    search_fields = ['event_name', 'event_date', 'manager']
    # add filter for post status and created_by date
    list_filter = ('event_date', 'manager')
    # summernote formatting to be applied to event's 'description' field
    summernote_fields = ('description')

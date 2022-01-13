from django.contrib import admin
from .models import Event, Venue, User
from django_summernote.admin import SummernoteModelAdmin


# decorator to register Venue admin class for admin site
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    # customise list view of admin panel
    list_display = ('venue_name', 'contact_no', 'address', 'venue_email')
    # add search fields for venue name
    search_fields = ['venue_name']


# decorator to register User admin class for admin site
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    # customise list view of admin panel
    list_display = ('first_name', 'last_name', 'user_email')
    # add search fields for either user's last name or email
    search_fields = ['last_name', 'user_email']
    # add filter for user's last name or email
    list_filter = ('last_name', 'user_email')


# decorator to register Event admin class for admin site
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    # customise list view of admin panel
    list_display = ('event_name', 'venue', 'event_date', 'manager')
    # add search fields for either event or date or manager
    search_fields = ['event_name', 'event_date', 'manager']
    # add filter for event date and manager
    list_filter = ('event_date', 'manager')
    # summernote formatting to be applied to event's 'description' field
    summernote_fields = ('description')

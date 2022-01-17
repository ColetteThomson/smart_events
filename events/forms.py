from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# create an event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        # fields to be imported from class Event
        fields = ('event_name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        # set the label to none
        labels = {
            'event_name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': '',
        }
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields to be imported from class Venue
        fields = ('venue_name', 'address', 'contact_no', 'website', 'venue_email')
        labels = {
            'venue_name': '',
            'address': '',
            'contact_no': '',
            'website': '',
            'venue_email': '',
        }
        widgets = {
            'venue_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'venue_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Venue Email'}),
        }

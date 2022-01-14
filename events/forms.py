from django import forms
from django.forms import ModelForm
from .models import Venue


# create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields to be imported from class Venue
        fields = ('venue_name', 'address', 'contact_no', 'website', 'venue_email')
        

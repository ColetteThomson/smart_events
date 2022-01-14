from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# ERD model for class Venue
class Venue(models.Model):
    venue_name = models.CharField(max_length=120)
    address = models.CharField(max_length=300)
    contact_no = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    venue_email = models.EmailField(blank=True)

    # helper method for class Venue:
    # returns a string representation of an object
    def __str__(self):
        return self.venue_name


# ERD model for class SiteUser
class SiteUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField()

    # helper method for class User:
    # returns a string representation of an object
    def __str__(self):
        return self.first_name + " " + self.last_name


#  ERD model for class Event
class Event(models.Model):
    event_name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    # to allow a new event to be added without a venue assigned
    # if one-to-many venue relationship is deleted so will all related records
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # sets manager field to null, should manager cease to be a user
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    # to allow an attendee to attend many events and
    # to allow an event to be saved without any attendees
    attendees = models.ManyToManyField(SiteUser, blank=True)
    # to set description field to optional
    description = models.TextField(blank=True)

    # helper method for class Event:
    # returns a string representation of an object
    def __str__(self):
        return self.event_name

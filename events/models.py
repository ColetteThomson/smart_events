from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

#  ERD model for class Event.
class Event(models.Model):
    event_name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    # set description field to optional
    description = models.TextField(blank=True)

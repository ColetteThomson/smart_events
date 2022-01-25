from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# ERD model for class Tech Support
class TechSupport(models.Model):
    person_name_TS = models.CharField(max_length=120)
    contact_no = models.CharField(max_length=20, blank=True)
    person_email = models.EmailField(blank=True)

    # helper method for class TechSupport:
    # returns a string representation of an object
    def __str__(self):
        return self.person_name_TS



# ERD model for class People
class People(models.Model):
    person_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=120)
    # address = models.CharField(max_length=300)
    contact_no = models.CharField(max_length=20, blank=True)
    # website = models.URLField(blank=True)
    person_email = models.EmailField(blank=True)
    # projects = models.ManyToOneField(blank=True)
    # if one-to-many project relationship is deleted so will all related records
    ### projects = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    
    # add owner (using user.id), must be an owner so default value
    owner = models.IntegerField("People Owner", blank=False, default=1)
 
    # helper method for class People:
    # returns a string representation of an object
    def __str__(self):
        return self.person_name


#  ERD model for class Project
class Project(models.Model):
    project_name = models.CharField(max_length=120)
    project_date = models.DateTimeField()
    # to allow a new project to be added without people assigned
    # if one-to-many people relationship is deleted so will all related records
    people = models.ForeignKey(People, blank=True, null=True, on_delete=models.CASCADE)
    resource_TS = models.ForeignKey(TechSupport(), blank=True, null=True, on_delete=models.CASCADE)
        
    ##job_title = models.ForeignKey(People, blank=True, null=True, on_delete=models.CASCADE)
    # sets manager field to null, should manager cease to be a user
    project_manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    # to allow an attendee to attend many events and
    # to allow an event to be saved without any attendees
    # attendees = models.ManyToManyField(SiteUser, blank=True)
    # to set description field to optional
    description = models.TextField(blank=True)

    # helper method for class Project:
    # returns a string representation of an object
    def __str__(self):
        return self.project_name


# ERD model for class SiteUser
class SiteUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField()

    # helper method for class User:
    # returns a string representation of an object
    def __str__(self):
        return self.first_name + " " + self.last_name

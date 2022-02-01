from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# ERD model for class Tech Support
class PeopleTechSupport(models.Model):
    person_name_tech = models.CharField(max_length=120)
    contact_no_tech = models.CharField(max_length=20, blank=True)
    person_email_tech = models.EmailField(blank=True)
    # sets project_experience field to mandatory
    project_experience = models.TextField(max_length=300, blank=False, default='experience')
    # sets ts_owner field to null, should ts_owner cease to be a user
    ts_owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # helper method for class PeopleTechSupport:
    # returns a string representation of an object
    def __str__(self):
        return self.person_name_tech


# ERD model for class People
class PeopleAdministration(models.Model):
    person_name = models.CharField(max_length=120)
    contact_no = models.CharField(max_length=20, blank=True)
    person_email = models.EmailField(blank=True)
    # sets project_experience field to mandatory
    project_experience = models.TextField(max_length=300, blank=False, default='experience')
    # sets ad_owner field to null, should owner cease to be a user
    ad_owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
     
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
    resource_admin = models.ForeignKey(PeopleAdministration, blank=True, null=True, on_delete=models.CASCADE)
    resource_tech = models.ForeignKey(PeopleTechSupport, blank=True, null=True, on_delete=models.CASCADE)
    # sets manager field to null, should manager cease to be a user
    project_manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # sets description field to mandatory
    description = models.TextField(max_length=300)

    # helper method for class Project:
    # returns a string representation of an object
    def __str__(self):
        return self.project_name

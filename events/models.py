from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# ERD model for class Tech Support
class PeopleTechSupport(models.Model):
    person_name_tech = models.CharField(max_length=120)
    contact_no_tech = models.CharField(max_length=20, blank=True)
    person_email_tech = models.EmailField(blank=True)
    #add owner (using user.id), must be an owner so default value
    ts_owner = models.IntegerField("Owner", blank=False, default=1)
    # sets manager field to null, should manager cease to be a user
    # ts_owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # helper method for class PeopleTechSupport:
    # returns a string representation of an object
    def __str__(self):
        return self.person_name_tech



# ERD model for class People
class PeopleAdmin(models.Model):
    person_name = models.CharField(max_length=120)
    contact_no = models.CharField(max_length=20, blank=True)
    person_email = models.EmailField(blank=True)
    # projects = models.ManyToOneField(blank=True)
    # if one-to-many project relationship is deleted so will all related records
    ### projects = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    
    # add owner (using user.id), must be an owner so default value
    ad_owner = models.IntegerField("Owner", blank=False, default=1)
    ###ad_owner = models.IntegerField("People Owner")

    # sets manager field to null, should manager cease to be a user
    #ad_owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
 
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
    resource_admin = models.ForeignKey(PeopleAdmin, blank=True, null=True, on_delete=models.CASCADE)
    resource_tech = models.ForeignKey(PeopleTechSupport, blank=True, null=True, on_delete=models.CASCADE)
        
    # sets manager field to null, should manager cease to be a user
    project_manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #project_manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
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

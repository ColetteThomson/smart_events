from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


 # ERD model for class Post  NEED TO CHANGE CLASS NAME!!!
#  class Post(models.Model):


#      # helper methods for class Post:
#      # order posts based on created_on field (in descending order)
#      class Meta:
#          ordering = ['-created_on']

#      # returns a string representation of an object
#      def __str__(self):
#          return self.blog_title
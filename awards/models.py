from django.db import models

from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from .models import Profile,Project,,Rating
# from . forms import ProfileUploadForm,CommentForm,ProfileForm,ImageForm,ImageUploadForm
from django.conf import settings




class Project(models.Model):
   title = models.CharField(max_length = 30,null = True)
   landing = models.CharField( max_length = 20,null = True)
   description = models.CharField(max_length = 100,null = True)
   link = models.CharField(max_length = 100,null = True)
   user = models.ForeignKey(User,null=True)
   image = models.ImageField(upload_to='images/', blank=True)
  
  

   def __str__(self):
       return self.name


   def save_project(self):
       self.save()

   @classmethod
   def all_projets(cls):
       projects = cls.objects.all()
       return projects

   @classmethod
   def get_project(cls, id):
       project = cls.objects.get(id=id)
       return project
  
   def __str__(self):
       return self.user.username

  
   @classmethod
   def search_by_title(cls,search_term):
       projec = cls.objects.filter(title__icontains=search_term)
       return projec
class Profile(models.Model):
   username = models.CharField(default='User',max_length=80)
   bio = models.CharField(max_length =30)
   image = models.ImageField(upload_to='images/', blank=True)
   contact = models.EmailField( max_length=90,null=True)
   user = models.ForeignKey(User,null=True)
#    Project= models.IntegerField(default=0)
   project = models.ForeignKey(Project,null=True)
   def __str__(self):
        return self.username

   def delete_profile(self):
        self.delete()

   def save_profile(self):
        self.save() 


   def __str__(self):
       return self.bio
class tags(models.Model):
   name = models.CharField(max_length =30)
  

   def __str__(self):
       return self.name



class PhotosLetterRecipients(models.Model):
   name = models.CharField(max_length = 30)
   email = models.EmailField()



class Rating(models.Model): 
       design = models.IntegerField( default=0)
       usability = models.IntegerField(default=0)
       content = models.IntegerField( default=0)
       project = models.ForeignKey(Project,null=True)
       project = models.ForeignKey(Project,null=True,related_name='rating')
       user = models.ForeignKey(User,null=True)
       image = models.ForeignKey(Profile,null= True)
      
       def __str__(self):
           return self.design
       
       def __str__(self):
           return self.usability

       def __str__(self):
           return self.content
  
       def save_rating(self):
           self.save()

       def save_design(self):
           self.save()

       def save_usability(self):
           self.save()
       def save_content(self):
           self.save()
class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)           
  






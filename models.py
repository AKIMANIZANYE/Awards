from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from .models import Profile, Image, Comment, Follow, Unfollow, Likes
# from . forms import ProfileUploadForm,CommentForm,ProfileForm,ImageForm,ImageUploadForm
from django.conf import settings

class Profile(models.Model):
    bio = models.CharField(max_length =30)
    image = models.ImageField(upload_to='images/', blank=True)
    Project = models.ForeignKey(Project,null=True)
    contact = models.EmailField(max_length=80,null=True)

    def __str__(self):
        return self.bio
class tags(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length = 30,null = True)
    landing = models.CharField(null = True)
    description = models.CharField(max_length = 100,null = True)
    link = models.CharField(max_length = 100,null = True)
    user = models.ForeignKey(User,null=True)
    Project = models.CharField(upload_to='images/', blank=True)

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
    def search_by_name(cls,search_term):
        projec = cls.objects.filter(name__icontains=search_term)
        return projec

class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField() 



class Rating(models.Model):
        design = models.CharField( null= True)
        usability   = models.CharField(max-length = 90,null=True)
        content = models.CharField( max-length = 90,null=True)
        Project = models.ForeignKey(Project,null=True)
        user = models.ForeignKey(User,null=True)
        
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
    

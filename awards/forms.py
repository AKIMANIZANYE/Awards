from django import forms
from .models import Project,Profile,Rating


class ProjectsLetterForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
        # widgets = {
        #     'profile': forms.CheckboxSelectMultiple(),
        # }
class ProfileForm(forms.ModelForm):
	# model = Profile
	# username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Project description',max_length=500)
	image = forms.ImageField(label = 'Image Field')
class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

class RatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		
		exclude = ['user','image',]

class ImageForm(forms.ModelForm):
	class Meta:
		model = Project
		
		exclude = ['user']

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Project
		
		exclude = ['user']
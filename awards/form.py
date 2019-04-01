from django import forms
from .models import Project


class ProjectsLetterForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user']
        # widgets = {
        #     'profile': forms.CheckboxSelectMultiple(),
        # }
class ProfileForm(forms.ModelForm):
	# model = Profile
	# username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Project description',max_length=500)
	image = forms.ImageField(label = 'Image Field')

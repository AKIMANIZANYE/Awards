from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Project,Profile,Rating
from .forms import ProjectsLetterForm, NewProjectForm,ProfileUploadForm,RatingForm,ProfileForm,ImageForm,ImageUploadForm
from django.contrib.auth.decorators import login_required
from django.conf import settings



@login_required(login_url = '/accounts/login/')
def post_today(request):
	title = 'Awwards'
	all_project = Project.objects.all()
	print(all_project)
	return render(request, 'all-projects/today-projects.html',  {"title":title, "projects":all_project})


def search_results(request):

	if 'project' in request.GET and request.GET["project"]:
			search_term = request.GET.get("project")
			searched_projects = Project.search_by_name(search_term)
			message = f"{search_term}"

			return render(request, 'all-projects/search.html',  {"message":message, "projects":searched_projects})

	else:
		message = "You haven't searched for any term"
	return render(request, 'all-projects/search.html',  {"message":message})

@login_required(login_url = '/accounts/login/')
def project(request, project_id):
	try:
		project = Project.objects.get(id = project_id)
	except DoesNotExist:
		raise Http404()
	return render(request, "all-projects/project.html",  {"project":project})

@login_required(login_url = '/accounts/login/')
def new_project(request):
	current_user = request.user
	title = 'New project'
	if request.method == 'POST':
		form = NewProjectForm(request.POST, request.FILES)
		if form.is_valid():
			project = form.save(commit = False)
			project.user = current_user
			project.save()
		return redirect('post_today')

	else:
		form = NewProjectForm()
	return render(request, 'new_project.html',  {"form":form, "current_user":current_user, "title":title})

@login_required(login_url='/accounts/login/')
def rating(request,id):
	
	post = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = RatingForm(request.POST)

		if form.is_valid():
			rating = form.save(commit=False)
			rating.user = current_user
			rating.image = post
			rating.save()
			return redirect('post_today')
	else:
		form = RatingForm()

	return render(request,'ratingt.html',{"form":form})  
@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	
	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile})
@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_image']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_image = form.cleaned_data['profile_image'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def upload_images(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
           
            image.save() 

            # return redirect( timeline)
    else:
        form = ImageForm() 
    return render(request, 'my-awwards/upload_images.html',{"form" : form})


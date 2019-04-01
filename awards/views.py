from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Project, ProjectsLetterRecipients
from .forms import ProjectsLetterForm, NewProjectForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/accounts/login/')
def post_today(request):
	date = dt.date.today()
	all_projects = Project.all_projects()
	projects = Project.objects.all()
	print(projects)

	if request.method == 'POST':
		form = ProjectsLetterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

			recipient = ProjectsLetterRecipients(name = name, email = email)
			recipient.save()
			send_welcome_email(name, email)

			HttpResponseRedirect('post_today')
	else:
		form = ProjectsLetterForm()
		form = NewProjectForm()
	return render(request, 'all-projects/today-projects.html',  {"date":date, "letterForm":form, "ProjectForm":form, "projects":all_projects})


def past_days_projects(request, past_date):

	try:
	# Converts data from the string Url
			date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
	except ValueError:
	# Raise 404 error when ValueError is thrown
		raise Http404()
		assert False

		if date == dt.date.today():
			return redirect(post_today)

	projects = Project.days_projects(date)
	return render(request, 'all-projects/past-projects.html',  {"date":date, "projects":projects})

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
		return redirect('projectsToday')

	else:
		form = NewProjectForm()
	return render(request, 'new_project.html',  {"form":form, "current_user":current_user, "title":title})


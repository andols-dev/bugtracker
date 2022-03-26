from django.shortcuts import get_object_or_404, render
from .models import Project,Bug
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm, createBugForm, BugMessageForm




@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'projects': projects})

@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    form = createBugForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.created_by = request.user
        form.project = project
        form.save()
    
    # this is a message on the bug not the project, maybe move this form to a bug detail page
    # project_message_form = projectMessageForm(request.POST or None)
    # if project_message_form.is_valid():
    #     message_form = form.save(commit=False)
    #     # id of the bug
    #     message_form.Bug = bug

    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'projects/project_detail.html', context)



def bug_detail(request,id):
    bug = get_object_or_404(Bug, id=id)
    bug_message_form = BugMessageForm(request.POST or None)
    if bug_message_form.is_valid():
        bug_message_form = bug_message_form.save(commit=False)
        # id of the bug
        bug_message_form.bug = bug
        bug_message_form.save()

    context = {'bug': bug, 'form': bug_message_form}

    return render(request, 'projects/bug_detail.html', context)



def create_Project(request): 
    form = CreateProjectForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'projects/create_project.html', context)
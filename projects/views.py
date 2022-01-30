from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def projects(request):

    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'projects': projects})

@login_required
def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/project_detail.html', {'project': project})
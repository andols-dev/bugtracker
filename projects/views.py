from django.shortcuts import render
from .models import Project
def projects(request):

    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'projects': projects})


def project_detail(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/project_detail.html', {'project': project})
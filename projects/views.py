from django.shortcuts import render
from .models import Project,Bug
from django.contrib.auth.decorators import login_required




@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{'projects': projects})

@login_required
def project_detail(request, id):
    project = Project.objects.get(id=id)
    project_members = project.member.all()
    project_bugs = Bug.objects.all().filter(project_id=id)
    unresolved_bugs = project_bugs.filter(state='UN').count()
    resolved_bugs = project_bugs.filter(state='RE').count()

    print(resolved_bugs)
    print(unresolved_bugs)
    context = {
        'project': project,
        'project_members':project_members,
       'unresolved_bugs': unresolved_bugs,
       'resolved_bugs': resolved_bugs,
       'project_bugs':project_bugs
    }
    return render(request, 'projects/project_detail.html', context)
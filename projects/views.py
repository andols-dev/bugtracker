from django.shortcuts import get_object_or_404, render
from .models import Project,Bug
from django.contrib.auth.decorators import login_required
from .forms import createBugForm




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
    print(form)

    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'projects/project_detail.html', context)
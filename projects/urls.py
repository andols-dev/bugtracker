
from django.urls import path
from .views import (projects, projects_list,project_detail,bug_detail,create_Project
)
urlpatterns = [
    path('',projects,name='projects'),
    path('detail/<int:id>/',project_detail, name='project-detail'),
    path('bugs/detail/<int:id>/',bug_detail, name='bug-detail'),
    path('create',create_Project,name='create-project'),
    path('projects/',projects_list,name="projects_list"),


]

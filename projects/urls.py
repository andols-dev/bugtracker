
from django.urls import path
from .views import (projects, project_detail,
    bug_detail
)
urlpatterns = [
    path('',projects,name='projects'),
    path('detail/<int:id>/',project_detail, name='project-detail'),
    path('bugs/detail/<int:id>/',bug_detail, name='bug-detail'),

]


from django.urls import path
from .views import projects, project_detail
urlpatterns = [
    path('',projects,name='projects'),
    path('detail/<int:id>/',project_detail, name='project-detail'),
]

from django import forms

from projects.models import Bug,Message, Project
class createBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name','description','priority','state']


class BugMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','member','lead']


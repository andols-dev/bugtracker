from django import forms

from projects.models import Bug,Message
class createBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name','description','priority','state']


class BugMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


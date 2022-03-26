from django import forms

from projects.models import Bug
class createBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['name','description','priority','state']
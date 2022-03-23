from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    lead = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='lead')
    member = models.ManyToManyField(User, related_name='member')
    objects = models.Manager()

    def unresolved_bugs(self):
        return self.bug_set.filter(state='UN')

    def resolved_bugs(self):
        return self.bug_set.filter(state='RE')

    def project_members(self):
        return self.member.all()

    def __str__(self):
        return self.name


class Bug(models.Model):
    PRIORITY_CHOICES = [
        ('LO', 'Low'),
        ('MD', 'Medium'),
        ('HI', 'High')
    ]
    STATE_CHOICES = [
        ('RE', 'Resolved'),
        ('UN', 'Unresolved')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.name

from django.forms import ModelForm
from .models import Project, TimeEntry


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'type']


class TimeEntryForm(ModelForm):
    class Meta:
        model = TimeEntry
        fields = '__all__'
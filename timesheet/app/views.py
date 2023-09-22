from django.shortcuts import render
from .models import Employee, TimeEntry, Project
from .forms import ProjectForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'app/employees.html', context)

def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'app/projects.html', context)


def project_add(request):
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'app/add_project.html', context)
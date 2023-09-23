from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')


    return render(request, 'app/add_project.html', context)


def project_delete(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('projects')


def project_edit(request, id):
    project = get_object_or_404(Project, id=id)
    form = ProjectForm(instance=project)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        form.save()
        return redirect('projects')

    return render(request, 'app/edit_project.html', context)
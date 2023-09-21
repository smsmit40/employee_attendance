from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def employee_list(request):
    return render(request, 'app/employees.html')

def project_list(request):
    return render(request, 'app/projects.html')
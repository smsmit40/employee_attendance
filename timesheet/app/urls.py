from django.urls import path
from .views import index, employee_list, project_list, project_add, project_delete, project_edit
urlpatterns = [
    path('', index, name='index'),
    path('employees/', employee_list, name='employees'),
    path('projects/', project_list, name='projects'),
    path('projects/add', project_add, name='add_project'),
    path('projects/delete/<int:id>/', project_delete, name='delete_project'),
    path('projects/edit/<int:id>/', project_edit, name='edit_project')
]

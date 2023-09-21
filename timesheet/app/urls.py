from django.urls import path
from .views import index, employee_list, project_list
urlpatterns = [
    path('', index, name='index'),
    path('employees/', employee_list, name='employees'),
    path('projects/', project_list, name='projects')
]

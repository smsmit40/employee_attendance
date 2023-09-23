from django.db import models


# Create your models here.
class Employee(models.Model):
    IT_SUPPORT = 'IS'
    INFRASTRUCTURE = 'IF'
    FINANCE = 'FI'
    ACCOUNTING = 'AC'
    DEVELOPERS = 'DE'
    SECURITY = 'SE'
    HUMAN_RESOURCES = 'HR'
    PRODUCT = 'PR'
    department_choices = [
        (IT_SUPPORT, "IT SUPPORT"),
        (INFRASTRUCTURE, "INFRASTRUCTURE"),
        (FINANCE, "FINANCE"),
        (ACCOUNTING, 'ACCOUNTING'),
        (DEVELOPERS, 'DEVELOPERS'),
        (SECURITY, "SECURITY"),
        (HUMAN_RESOURCES, "HUMAN RESOURCES"),
        (PRODUCT, "PRODUCT")
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=2, choices=department_choices)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    CAPEX = "CA"
    OPEX = 'OP'
    project_type_choices = [
        (CAPEX, 'CAPEX'),
        (OPEX, 'OPEX')
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=project_type_choices)

    def __str__(self):
        return self.name


class TimeEntry(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hours = models.IntegerField(null=False, default=1)
    date = models.DateField()

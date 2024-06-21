from django.db import models
from django.db.models import Q, F

class Employees(models.Model):
    departments = models.CharField(max_length=120)
    department_1 = models.IntegerField()
    department_2 = models.IntegerField()

    def __str__(self):
        return self.departments


instance_1 = Employees.objects.filter(department_1__gt=F("department_2"))


instance_2 = Employees.objects.filter(Q(department_1__gt=20) | Q(department_2__gt=20))

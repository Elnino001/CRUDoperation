from django.db import models
from django.urls import reverse

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=40)
    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    pmp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    
    def get_absolute_url(self):
        return reverse("employee_list",kwargs={'pk':self.pk})



from django.dispatch import receiver


from django.db import models

# Create your models here.
# class Position(models.Model):
#     title = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    con_password = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    # position = models.ForeignKey(Position,on_delete = models.CASCADE)









from django.db import models

# Create your models here.
# class Position(models.Model):
#     title = models.CharField(max_length=50)


class data(models.Model):
    height = models.CharField(max_length=1000)
    weight = models.CharField(max_length=1000)
    sex = models.CharField(max_length=30)
    age = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    # position = models.ForeignKey(Position,on_delete = models.CASCADE)
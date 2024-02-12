from django.db import models

# Create your models here.
# class Position(models.Model):
#     title = models.CharField(max_length=50)


class chart(models.Model):
    breakfast = models.CharField(max_length=1000)
    lunch = models.CharField(max_length=1000)
    snacks = models.CharField(max_length=1000)
    dinner = models.CharField(max_length=1000)
    Notes = models.CharField(max_length=1000)
    
    
    # position = models.ForeignKey(Position,on_delete = models.CASCADE)
from django.db import models

# Create your models here.
class position(models.Model):
    title = models.CharField(max_length=50)

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    con_password = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    postition = models.ForeignKey(position, on_delete = models.CASCADE)


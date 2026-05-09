from django.db import models

# Create your models here.
class Teacher(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=30, null=False)
    number = models.BigIntegerField(unique=True, null=False)
    email = models.EmailField(null=True)
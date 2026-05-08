from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=35, null=False)
    number = models.BigIntegerField(null=False)
    email = models.EmailField()
    percentage = models.FloatField() 
from django.db import models

# Create your models here.

class TestModel(models.Model):

    DEPARTMENT =  ((1,'CIVIL'),(2,'COMPUTER'),(3,'IT'),(4,'SOFTWARE'))
    name = models.CharField(max_length=255)
    department = models.IntegerField(choices=DEPARTMENT)
    roll_num = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


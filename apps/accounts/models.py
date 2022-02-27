from django.db import models
from django.contrib.auth.models import User

class BasicUserProfile(models.Model):

    age = models.IntegerField(blank=True,null=True)
    dateofbirth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=20,default='male')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
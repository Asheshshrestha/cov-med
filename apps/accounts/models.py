from django.db import models
from django.contrib.auth.models import User

class BasicUserProfile(models.Model):

    age = models.IntegerField()
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

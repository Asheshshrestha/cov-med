from email.policy import default
from django.db import models
from sqlalchemy import true

# Create your models here.

class HospitalServiceModule(models.Model):

    service_name = models.CharField(max_length=255,unique=True)
    service_desc = models.TextField(max_length=1040)
    is_ineffect = models.BooleanField(default=true)
    service_image = models.ImageField(upload_to='services',default='services/default_service.png')
    service_icon = models.CharField(max_length=100,blank=True)
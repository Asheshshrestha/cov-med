from distutils.command.upload import upload
from turtle import up
from django.db import models
from apps.services.models import HospitalServiceModule
# Create your models here.
class HospitalModel(models.Model):

    hospital_name = models.CharField(max_length=225)
    hospital_code = models.CharField(max_length=20,unique=True)
    in_service = models.BooleanField(default=True)
    hospital_provience = models.CharField(max_length=255)
    hospital_city = models.CharField(max_length=255)
    hospital_location = models.CharField(max_length=255)
    emergency_phone = models.TextField(max_length=1024)
    reception_phone = models.TextField(max_length=1024,blank=True,null=True)
    hospital_map_location_url = models.URLField(max_length=300,blank=True,null=True)
    hospital_services = models.ManyToManyField(HospitalServiceModule)
    hospital_webiste_url = models.URLField(max_length=500,blank=True,null=True)
    hospital_logo = models.ImageField(upload_to='hospital/logo',default='hospital/default.png',blank=True,null=True)
    hospital_image = models.ImageField(upload_to='hospital/images',default='hospital/default.png',blank=True,null=True)
    hospital_description = models.TextField(max_length=1040,blank=True,null=True)

    def __str__(self):
        return self.hospital_name
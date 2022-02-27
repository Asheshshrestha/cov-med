from django.db import models

# Create your models here.

class HospitalServiceModule(models.Model):

    service_name = models.CharField(max_length=255,unique=True)
    service_desc = models.TextField(max_length=1040)
    is_ineffect = models.BooleanField(default=True)
    service_image = models.ImageField(upload_to='services',default='services/default_service.png')
    service_icon = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.service_name
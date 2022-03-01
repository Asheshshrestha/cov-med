from django.db import models
from django.contrib.auth.models import User
from apps.hospital.models import HospitalModel

class BasicUserProfile(models.Model):

    age = models.IntegerField(blank=True,null=True)
    dateofbirth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=20,default='male')
    reffer_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    #personal informations
    median_name = models.CharField(max_length=10,blank=True,null=True)
    personal_phone_no = models.CharField(max_length=20,blank=True,null=True)
    office_phone_no = models.CharField(max_length=20,blank=True,null=True)
    permanent_address = models.CharField(max_length=255,blank=True,null=True)
    current_address = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    private_gmail = models.EmailField(null=True)
    profile_image = models.ImageField(upload_to='doctor/profile_image',default='hospital/default.png',blank=True,null=True)

    #doctor information
    doctor_regestriation_no = models.CharField(max_length=255,null=True)
    medical_specialties = models.CharField(max_length=255,blank=True,null=True)
    hospital = models.ForeignKey(HospitalModel,on_delete=models.DO_NOTHING,null=True)
    job_type = models.CharField(max_length=255,blank=True,null=True)
    availablility = models.CharField(max_length=255,blank=True,null=True)
    highest_degree = models.CharField(max_length=255,blank=True,null=True)
    studied_in = models.CharField(max_length=255,blank=True,null=True)
    doctor_licence = models.FileField(upload_to='doctor/licence_image',blank=True,null=True)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.reffer_user

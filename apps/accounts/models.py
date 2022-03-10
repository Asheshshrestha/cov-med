from django.db import models
from django.contrib.auth.models import User
from apps.hospital.models import HospitalModel

class BasicUserProfile(models.Model):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'),('other','Other')]
    MEDICAL_SPECIALS = [('dermatologists','Dermatologists'),
                        ('Infectious_disease_doctors','Infectious disease doctors'),
                        ('ophthalmologists','Ophthalmologists'),
                        ('obstetrician','Obstetrician'),
                        ('cardiologists','Cardiologists'),
                        ('endocrinologists','Endocrinologists'),
                        ('gastroenterologists','Gastroenterologists'),
                        ('nephrologists','Nephrologists'),
                        ('urologists','Urologists'),
                        ('pulmonologists','Pulmonologists'),
                        ('rheumatologists','Rheumatologists'),
                        ('radiologists','Radiologists'),
                        ('oncologists','Oncologists'),
                        ('psychiatrists','Psychiatrists'),
                        ('neurologists','Neurologists'),
                        ('otolaryngologists','Otolaryngologists'),
                        ('anesthesiologists','Anesthesiologists')
                        ]
    JOB_TYPE_CHOICES = [('fulltime','Full Time'),('parttime','Part Time')]
    AVAILABILITY_CHOICES = [('anytime','Anytime'),('onshift','ON Shift')]
    HIGHEST_DEGREE_CHOICES = [('mbbs','M.B.B.S'),('md','M.D')]
    STUDIED_CHOICES = [('incountry','In Country'),('outcountry','Out Country')]

    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    dateofbirth = models.DateField(blank=True,null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=20,default='male')
    reffer_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    #personal informations
    median_name = models.CharField(max_length=10,blank=True,null=True)
    personal_phone_no = models.CharField(max_length=20,blank=True,null=True)
    office_phone_no = models.CharField(max_length=20,blank=True,null=True)
    permanent_address = models.CharField(max_length=255,blank=True,null=True)
    current_address = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    private_gmail = models.EmailField(null=True)
    profile_image = models.ImageField(upload_to='doctor/profile_image',default='hospital/default.png',null=True)

    #doctor information
    doctor_regestriation_no = models.CharField(max_length=255,null=True)
    medical_specialties = models.CharField(choices=MEDICAL_SPECIALS,max_length=255,blank=True,null=True)
    hospital = models.ForeignKey(HospitalModel,on_delete=models.DO_NOTHING,null=True)
    job_type = models.CharField(choices=JOB_TYPE_CHOICES,max_length=255,blank=True,null=True)
    availablility = models.CharField(choices= AVAILABILITY_CHOICES,max_length=255,blank=True,null=True)
    highest_degree = models.CharField(choices=HIGHEST_DEGREE_CHOICES,max_length=255,blank=True,null=True)
    studied_in = models.CharField(choices=STUDIED_CHOICES,max_length=255,blank=True,null=True)
    doctor_licence = models.FileField(upload_to='doctor/licence_image',blank=True,null=True)
    is_doctor = models.BooleanField(default=False)
    appointment_per_day = models.IntegerField(default=50,null=True,blank=True)
    # def __str__(self):
    #     return self.reffer_user.username

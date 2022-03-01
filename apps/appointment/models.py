from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppointmentModel(models.Model):

    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'),('other','Other')]
    patient_first_name = models.CharField(max_length=255)
    patient_last_name = models.CharField(max_length=255)
    patient_age = models.IntegerField()
    patient_phone_number = models.CharField(max_length=20)
    patient_location = models.CharField(max_length=255)
    patient_gender = models.TextField(choices=GENDER_CHOICES,max_length=20)
    appointment_date = models.DateField(null=True,blank=True)
    appointment_time = models.TimeField(null=True,blank=True)
    symptom_description = models.TextField(max_length=1025)
    apply_date = models.DateField(auto_now_add=True)
    has_already_appointed = models.BooleanField(default=False)
    report_file = models.FileField(upload_to='doctor/appointment/report',default='hospital/default.png',blank=True,null=True)
    reffer_user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient',null=True)
    reffer_doctor = models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor',null=True)

    def __str__(self):
        return self.patient_first_name+' '+self.patient_last_name+ '( Dr. '+self.reffer_doctor.first_name+' '+self.reffer_doctor.last_name+')'
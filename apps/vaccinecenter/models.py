from django.db import models

# Create your models here.
class CoronaVaccineCenter(models.Model):

    PROVIENCE_CHOICES = [('Provience 1','Provience 1'),
                        ('Madesh','Madesh'),
                        ('Bagmati','Bagmati'),
                        ('Gandaki','Gandaki'),
                        ('Lumbini','Lumbini'),
                        ('Karnali','Karnali'),
                        ('Sudurpashchim','Sudurpashchim')]
    VACCINE_TYPE_CHOICES = [('First','First'),
                            ('Second','Second'),
                            ('Booster','Booster'),
                            ('Other','Other')]
    SERVICE_TYPE = [('First Come First','First Come First'),
                    ('Anytime Sevice','Anytime Service'),
                    ('Specific People','Specific People')]
    center_name = models.CharField(max_length=255)
    provience = models.CharField(choices=PROVIENCE_CHOICES,max_length=50)
    district = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255,blank=True,null=True)
    map_url = models.URLField(blank=True,null=True)
    help_phone_no = models.CharField(max_length=1024,blank=True,null=True)
    vaccine_name = models.CharField(max_length=255)
    vaccine_batch = models.CharField(max_length=50,blank=True,null=True)
    vaccine_type = models.CharField(choices=VACCINE_TYPE_CHOICES,max_length=255,blank=True,null=True)
    age_group = models.BooleanField(default=True)
    age_from = models.IntegerField(blank=True,null=True)
    age_to = models.IntegerField(blank=True,null=True)
    provide_from = models.DateField()
    provide_to = models.DateField()
    service_type = models.CharField(choices=SERVICE_TYPE,max_length=255)
    is_quota = models.BooleanField(default=False)
    quota_quantity = models.IntegerField(blank=True,null=True)
    in_effect = models.BooleanField(default=True)


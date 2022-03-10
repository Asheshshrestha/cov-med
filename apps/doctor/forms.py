from enum import unique
from random import choice
from django import forms
from django.contrib.auth.models import User
from apps.accounts.models import BasicUserProfile
from apps.hospital.models import HospitalModel
from django.contrib.admin.widgets import FilteredSelectMultiple


class EmailValidation(forms.EmailField):
    def validate(self, value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already Exists")
        except User.DoesNotExist as e:
            pass

        except Exception as e:
            raise forms.ValidationError("Email already Exists")

class DoctorSignupForm(forms.Form):
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

    email = EmailValidation(required=True)
    username = forms.CharField(max_length=255,required=True)
    first_name = forms.CharField(required=True,max_length=255)
    last_name = forms.CharField(required=True,max_length=255)
    age = forms.IntegerField(required=True,min_value=1,max_value=100)
    dateofbirth = forms.DateField(required=True,widget=forms.TextInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    median_name = forms.CharField(required=False,max_length=255)
    personal_phone_no = forms.CharField(required=True,max_length=200)
    office_phone_no = forms.CharField(required=False,max_length=200)
    permanent_address = forms.CharField(required=False,max_length=255)
    current_address = forms.CharField(required=True,max_length=255)
    doctor_regestriation_no = forms.CharField(max_length=255,required=True)
    country = forms.CharField(max_length=255,required=True)
    private_gmail = forms.EmailField(required=True,max_length=255)
    profile_image = forms.ImageField(required=False)
    medical_specialties = forms.ChoiceField(choices=MEDICAL_SPECIALS)
    hospital = forms.ModelChoiceField(
        queryset=HospitalModel.objects.all(),
        required=True
    )
    job_type = forms.ChoiceField(choices=JOB_TYPE_CHOICES)
    availablility = forms.ChoiceField(choices=AVAILABILITY_CHOICES)
    highest_degree = forms.ChoiceField(choices=HIGHEST_DEGREE_CHOICES)
    studied_in = forms.ChoiceField(choices=STUDIED_CHOICES)
    doctor_licence = forms.FileField(required=False)
    class Media:
        css = {'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n/',)


class DoctorUpdateForm(forms.ModelForm):

    class Meta:
        model = BasicUserProfile
        fields = '__all__'
        
    
    
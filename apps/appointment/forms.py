from urllib import request
from django import forms
from setuptools import Require
from apps.appointment.models import AppointmentModel

class AppointmentModelForm(forms.ModelForm):

    appointment_date = forms.DateField(required=True,widget=forms.TextInput(attrs={'type':'date'}))
    appointment_time = forms.TimeField(required=True,widget=forms.TextInput(attrs={'type':'time'}))
    patient_location = forms.CharField(required=False)
    report_file = forms.FileField(required=False)
    has_already_appointed = forms.BooleanField(required=False)
    class Meta:
        model = AppointmentModel
        fields = ['patient_first_name',
                  'patient_last_name',
                  'patient_age',
                  'patient_phone_number',
                  'patient_location',
                  'patient_gender',
                  'appointment_date',
                  'appointment_time',
                  'symptom_description',
                  'has_already_appointed',
                  'report_file']
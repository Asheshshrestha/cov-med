from django import forms
from django.forms import TextInput,Textarea
from apps.vaccinecenter.models import CoronaVaccineCenter

class CoronaVaccineCenterFrom(forms.ModelForm):
    provide_from = forms.DateField(required=True,widget=forms.TextInput(attrs={'type':'date'}))
    provide_to = forms.DateField(required=True,widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = CoronaVaccineCenter
        fields = '__all__'
        labels = {
            "center_name": "Service Center Name",
            "map_url":"Map URL",
            "help_phone_no":"Contact No",
            "vaccine_name":"Vaccine Name",
            "vaccine_batch":"Vaccine Batch",
            "age_group":"For Age Group?",
            "age_from":"Age From",
            "age_to":"Age To",
            "provide_from":"Provided From",
            "provide_to":"Provided To",
            "service_type":"Service Type",
            "is_quota":"Has Quota?",
            "quota_quantity":"Quota Quantity",
            "in_effect":"In Service"
        }
        widgets = {
            'help_phone_no': Textarea(attrs={'placeholder': 'Enter Your Service Phone No'})
        }
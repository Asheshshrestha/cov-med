from django import forms
from django.forms import TextInput,Textarea
from apps.services.models import HospitalServiceModule

class HospitalServiceModuleForm(forms.ModelForm):

    class Meta:
        model = HospitalServiceModule
        fields = '__all__'
        labels = {
            "service_name": "Service Name",
            "service_desc":"Description",
            "is_ineffect":"Active",
            "service_image":"Poster Image",
            "service_icon":"Display Icon"
        }
        widgets = {
            'service_name': TextInput(attrs={'placeholder': 'Enter Your Service Name'}),
            'service_desc': Textarea(attrs={'placeholder': 'Enter Your Service Description'}),
            'service_icon': TextInput(attrs={'placeholder': 'Eg. <i class="fas fa-trash-alt"></i>'}),
        }
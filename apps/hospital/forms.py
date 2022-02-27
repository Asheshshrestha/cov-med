from django import forms
from apps.hospital.models import HospitalModel
from apps.services.models import HospitalServiceModule
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import TextInput,Textarea
# Create your views here.

class HospitalModelForm(forms.ModelForm):

    hospital_services = forms.ModelMultipleChoiceField(
        queryset=HospitalServiceModule.objects.all(),
        widget = FilteredSelectMultiple('permissions',is_stacked=False)
    )
    class Media:
        css = {'all': ('/static/admin/css/widgets.css',),}
        js = ('/admin/jsi18n/',)
    class Meta:
        model = HospitalModel
        fields = '__all__'
        labels = {"hospital_name":"Hospital Name",
                  "hospita_code":"Hospital Code",
                  "hospital_provience":"Hospital Provience",
                  "hospital_city":"City",
                  "hospital_location":"Location",
                  "emergency_phone":"Emergency HotLine Phone No.",
                  "reception_phone":"Reception Phone No.",
                  "hospital_map_location_url":"Map Location URL",
                  "hospital_webiste_url":"Website URL",
                  "hospital_description":"Description",
                  "hospital_image":"Banner Image",
                  "hospital_logo":"Logo",
                  "hospital_services":"Major Services",
                  }
        widgets = {
            'hospital_name': TextInput(attrs={'placeholder': 'Enter Your Hospital Name'}),
            'hospital_code': TextInput(attrs={'placeholder': 'Enter Your Hospital Code.'}),
            'hospital_provience': TextInput(attrs={'placeholder': 'Enter Your Hospital Provience'}),
            'hospital_city': TextInput(attrs={'placeholder': 'Enter Your Hospital City'}),
            'hospital_location': TextInput(attrs={'placeholder': 'Enter Your Hospital Location'}),
            'emergency_phone': Textarea(attrs={'placeholder': 'Enter Your Phone No.'}),
            'reception_phone': Textarea(attrs={'placeholder': 'Enter Your Phone No.'}),
            'hospital_map_location_url': TextInput(attrs={'placeholder': 'Enter Your Hospital Map url'}),
            'hospital_webiste_url': TextInput(attrs={'placeholder': 'Enter Your Hospital Website URL'}),
            'hospital_description': Textarea(attrs={'placeholder': 'Enter Your Hospital Description'}),
        }

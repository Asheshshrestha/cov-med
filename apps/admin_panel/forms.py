from django import forms
from django.forms import widgets
from django.forms import fields
from apps.admin_panel.models import WebsiteSettingModel

class WebsiteSettingForm(forms.ModelForm):

    class Meta:

        model = WebsiteSettingModel
        fields = '__all__'

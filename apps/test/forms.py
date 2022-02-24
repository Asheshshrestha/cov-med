from django import forms 
from apps.test.models import TestModel

class TestCreateForm(forms.ModelForm):

    class Meta:
        model = TestModel
        fields = '__all__'
from django import forms 
from django.contrib.auth.models import Group,Permission,User
from django.contrib.admin.widgets import FilteredSelectMultiple

class GroupCreateForm(forms.ModelForm):

    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget = FilteredSelectMultiple('permissions',is_stacked=False)
    )
    class Media:
        css = {'all': ('/static/admin/css/widgets.css',),}
        js = ('/admin/jsi18n/',)

    class Meta:
        model = Group
        fields = '__all__'
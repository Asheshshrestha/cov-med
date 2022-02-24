from django import forms
from django.contrib.auth.models import Group,Permission,User
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms import fields

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32,widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    def validate(self,password, confirm_password):
        if password != confirm_password:
                raise forms.ValidationError("Both password must be same")

    password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    
class EmailValidation(forms.EmailField):
    def validate(self, value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already Exists")
        except User.DoesNotExist as e:
            pass

        except Exception as e:
            raise forms.ValidationError("Email already Exists")

class SignupForm(forms.ModelForm):
    email = EmailValidation(required=True)
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget = FilteredSelectMultiple('Groups',is_stacked=False),
        required=False
    )
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].initial = False
        self.fields['password'].initial = 'Test@123'

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n/',)
    class Meta:

        model = User
        fields = ('username',
                    'password',
                    'groups',
                    'is_superuser',
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff',
                    'is_active')

class UserUpadteForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget = FilteredSelectMultiple('Groups',is_stacked=False),
        required=False
    )

    class Media:
        css = {'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n/',)
    class Meta:

        model = User
        fields = ('username',
                    'groups',
                    'is_superuser',
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff',
                    'is_active')



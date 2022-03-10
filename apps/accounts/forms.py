from email.policy import default
from enum import unique
from django import forms
from django.contrib.auth.models import Group,Permission,User
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models.query import QuerySet
from django.forms import ValidationError, widgets
from django.forms import fields

class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=300)
    
class LoginForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32,widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    def validate(self,password, confirm_password):
        if password != confirm_password:
                raise forms.ValidationError("Both password must be same")
    password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    
class ChangePasswordDashboardForm(forms.Form):
    
    current_password = forms.CharField(max_length=32,widget=forms.PasswordInput)
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
class UserSignupForm(forms.Form):

    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'),('other','Other')]

    email = EmailValidation(required=True)
    username = forms.CharField(max_length=255,required=True)
    password = forms.CharField(max_length=32, required=True,widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=32, required=True,widget=forms.PasswordInput)
    first_name = forms.CharField(required=True,max_length=255)
    last_name = forms.CharField(required=True,max_length=255)
    age = forms.IntegerField(required=True,min_value=1,max_value=100)
    dateofbirth = forms.DateField(required=True,widget=forms.TextInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
           raise forms.ValidationError('Password must match to each other.')
                
class UserUpdateForm(forms.Form):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'),('other','Other')]

    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'readonly':'true'}))
    username = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'readonly':'true'}))
    first_name = forms.CharField(required=True,max_length=255)
    last_name = forms.CharField(required=True,max_length=255)
    age = forms.IntegerField(required=True,min_value=1,max_value=100)
    dateofbirth = forms.DateField(required=True,widget=forms.TextInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,)

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



from cgitb import reset
from tkinter import Menu
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ValidationError
from django.http import HttpRequest, request
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from gronckle_enginee import settings
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from apps.accounts.forms import (SignupForm,
                                UserUpadteForm,
                                ResetPasswordForm,
                                ChangePasswordDashboardForm,
                                UserSignupForm,UserUpdateForm,
                                PasswordResetForm)
from django.contrib.auth.hashers import check_password
from django.core.files import File
from apps.accounts.models import BasicUserProfile
from django.contrib.auth.models import Group
import string    
import random
from apps.accounts.models import BasicUserProfile
from apps.doctor.forms import DoctorSignupForm,DoctorUpdateForm
from apps.hospital.models import HospitalModel
from django.core.mail import send_mail
from gronckle_enginee.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin



class DoctorListView(PermissionRequiredMixin,ListView):
    template_name = 'admin/c-panel/pages/doctor/index.html'

    model = BasicUserProfile
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
    def get_queryset(self,*args,**kwargs):

        qs = super(DoctorListView,self).get_queryset(*args,**kwargs)
        qs = qs.filter(reffer_user__is_active=True).filter(is_doctor=True).order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Doctor Management' 
        return context


class AddDoctor(PermissionRequiredMixin,View):
    
    template_name = 'admin/c-panel/pages/doctor/manage.html'
    
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser

    def get(self,request,*args,**kwargs):
        form = DoctorSignupForm()
        return render(request,self.template_name,{'form':form,
                                                  'nav_link':'medcore',
                                                  'page_name':'Doctor Management'})

    def post(self,request):
        form = DoctorSignupForm(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            firs_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            age = form.cleaned_data.get('age')
            dateofbirth = form.cleaned_data.get('dateofbirth')
            gender = form.cleaned_data.get('gender')
            median_name = form.cleaned_data.get('median_name')
            personal_phone_no = form.cleaned_data.get('personal_phone_no')
            office_phone_no = form.cleaned_data.get('office_phone_no')
            permanent_address = form.cleaned_data.get('permanent_address')
            current_address = form.cleaned_data.get('current_address')
            country = form.cleaned_data.get('country')
            private_gmail = form.cleaned_data.get('private_gmail')
            profile_image = form.cleaned_data.get('profile_image')
            medical_specialties = form.cleaned_data.get('medical_specialties')
            hospital = form.cleaned_data.get('hospital')
            job_type = form.cleaned_data.get('job_type')
            availablility = form.cleaned_data.get('availablility')
            highest_degree = form.cleaned_data.get('highest_degree')
            studied_in = form.cleaned_data.get('studied_in')
            doctor_licence = form.cleaned_data.get('doctor_licence')
            doctor_regestriation_no = form.cleaned_data.get('doctor_regestriation_no')
            random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 12)) 
            if len(random_password) == 12:
                new_user = User.objects.create_user(username,email,random_password)
                new_user.first_name = firs_name
                new_user.last_name = last_name
                new_user.is_staff = True
                new_user.is_active = True
                new_user.save()
                user_group = Group.objects.get(name='Doctor')
                user_group.user_set.add(new_user)
                user_profile = BasicUserProfile(age = age,
                                                dateofbirth = dateofbirth,
                                                gender = gender,
                                                reffer_user = new_user,
                                                median_name = median_name,
                                                personal_phone_no = personal_phone_no,
                                                office_phone_no = office_phone_no,
                                                permanent_address = permanent_address,
                                                current_address = current_address,
                                                country = country,
                                                private_gmail = private_gmail,
                                                profile_image = profile_image,
                                                medical_specialties = medical_specialties,
                                                hospital = hospital,
                                                job_type = job_type,
                                                availablility = availablility,
                                                highest_degree = highest_degree,
                                                studied_in = studied_in,
                                                doctor_licence = doctor_licence,
                                                doctor_regestriation_no=doctor_regestriation_no,
                                                first_name = firs_name,
                                                last_name = last_name,
                                                is_doctor = True)
                user_profile.save()

                send_mail(
                        subject='Welcome'+ firs_name + ' '+ last_name +' to MedCore,',
                        message='Your doctor account is successfully created in Medcore pleact login with following credentials\nUsername: '+username +'\nPassword: '+ random_password+'\n Thank you.\n\n Please do not share this credential to any one.',
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[email],
                        fail_silently=True,
                    )   
                
                messages.success(request,'Successfully created doctor account.')
                return HttpResponseRedirect('/c-admin/doctor/list/')
            else:
                print('not valid password')
                messages.error(request,'Cannot create doctor account please try again later.')
                return render(request,self.template_name,{'form':form,
                                                        'nav_link':'medcore',
                                                        'page_name':'Doctor Management'})
        else:
            print('not valid')
            messages.warning(request,'Cannot create doctor account please try again later.')
            return render(request,self.template_name,{'form':form,
                                                        'nav_link':'medcore',
                                                        'page_name':'Doctor Management'})
class UpdateDoctor(PermissionRequiredMixin,View):
    
    template_name = 'admin/c-panel/pages/doctor/update.html'
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
         
    def get(self,request,pk,*args,**kwargs):
        profile = BasicUserProfile.objects.get(id=pk)
        form = DoctorUpdateForm(instance= profile)
        return render(request,self.template_name,{'form':form,
                                                  'nav_link':'medcore',
                                                  'page_name':'Doctor Management'})

    def post(self,request,pk):
        form = DoctorUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            firs_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            age = form.cleaned_data.get('age')
            dateofbirth = form.cleaned_data.get('dateofbirth')
            gender = form.cleaned_data.get('gender')
            median_name = form.cleaned_data.get('median_name')
            personal_phone_no = form.cleaned_data.get('personal_phone_no')
            office_phone_no = form.cleaned_data.get('office_phone_no')
            permanent_address = form.cleaned_data.get('permanent_address')
            current_address = form.cleaned_data.get('current_address')
            country = form.cleaned_data.get('country')
            doctor_regestriation_no = form.cleaned_data.get('doctor_regestriation_no')
            private_gmail = form.cleaned_data.get('private_gmail')
            profile_image = form.cleaned_data.get('profile_image')
            medical_specialties = form.cleaned_data.get('medical_specialties')
            hospital = form.cleaned_data.get('hospital')
            job_type = form.cleaned_data.get('job_type')
            availablility = form.cleaned_data.get('availablility')
            highest_degree = form.cleaned_data.get('highest_degree')
            studied_in = form.cleaned_data.get('studied_in')
            doctor_licence = form.cleaned_data.get('doctor_licence') 
            
            profile = BasicUserProfile.objects.get(id=pk)
            profile.first_name = firs_name
            profile.last_name = last_name
            profile.age = age
            profile.dateofbirth = dateofbirth
            profile.gender = gender
            profile.median_name = median_name
            profile.personal_phone_no = personal_phone_no
            profile.office_phone_no = office_phone_no
            profile.permanent_address = permanent_address
            profile.current_address = current_address
            profile.country = country
            profile.private_gmail = private_gmail
            profile.doctor_regestriation_no = doctor_regestriation_no
            profile.profile_image = profile_image
            profile.medical_specialties = medical_specialties
            profile.hospital = hospital
            profile.job_type = job_type
            profile.availablility = availablility
            profile.highest_degree = highest_degree
            profile.studied_in = studied_in
            profile.doctor_licence = doctor_licence
            profile.save()
            
            user = User.objects.get(id = profile.reffer_user.id)
            user.first_name = firs_name
            user.last_name = last_name
            user.save()
                                
           
            messages.success(request,'Successfully updated account.')
            return HttpResponseRedirect('/c-admin/doctor/list/')
           
        else:
            print('not valid')
            messages.warning(request,'Cannot create doctor account please try again later.')
            return render(request,self.template_name,{'form':form,
                                                        'nav_link':'medcore',
                                                        'page_name':'Doctor Management'})


class DeleteDoctor(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'admin/c-panel/pages/doctor/delete.html'
    success_message = "Doctor Delete Successfully."
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('doctor_index')
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
         
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(BasicUserProfile,id=id_)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Doctor Management' 
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteDoctor, self).delete(request, *args, **kwargs)
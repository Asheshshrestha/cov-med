from django.forms import fields
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,UpdateView,DetailView
from apps.admin_panel.models import WebsiteSettingModel
from apps.admin_panel.forms import WebsiteSettingForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from apps.hospital.models import HospitalModel
from gronckle_enginee import settings
from apps.accounts.models import BasicUserProfile
from apps.appointment.models import AppointmentModel
from apps.services.models import HospitalServiceModule
import requests
import json

class GIndex(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):

    template_name = 'admin/c-panel/pages/index/index.html'
    login_url = settings.LOGIN_URL

    def has_permission(self):
        return self.request.user.is_staff or self.request.user.has_perm('admin_panel.view_dashboard')
    def get_context_data(self, **kwargs):
        doctors_count = len(BasicUserProfile.objects.filter(is_doctor = True))
        hospital_count = len(HospitalModel.objects.filter(in_service=True))
        appointment_count = len(AppointmentModel.objects.all())
        service_count = len(HospitalServiceModule.objects.filter(is_ineffect=True))
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'index' 
        context["page_name"] = 'Dashboard' 
        context["doctor_count"] = doctors_count
        context["hospital_count"] = hospital_count
        context["appointment_count"] = appointment_count
        context["service_count"] = service_count
        context["corona_summary"] = get_coronacasesummary()
        return context

class GDetailSetting(PermissionRequiredMixin,DetailView):
    template_name = 'admin/c-panel/pages/settings/sitesetting.html'

    def has_permission(self):
        return self.request.user.is_superuser

    def get_object(self):
        return WebsiteSettingModel.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'settings' 
        context["page_name"] = 'Website Setting' 
        return context

class GUpdateSetting(SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
    model = WebsiteSettingModel
    form_class = WebsiteSettingForm
    template_name = 'admin/c-panel/pages/settings/update_setting.html'
    success_message = "Page Setting Updated Successfully."
    def has_permission(self):
        return self.request.user.is_superuser

    def get_object(self, *args, **kwargs):
        return WebsiteSettingModel.objects.first()
    
    def form_valid(self,form):
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return '/c-admin/settings/'
    

def get_coronacasesummary():
    try:
        url = "https://corona.askbhunte.com/api/v1/data/nepal"

        payload={}
        headers = {
        'Content-Type': 'application/json'
        }

        res = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(res.text)
    except:
        response = {"tested_positive":"N/A","tested_total":"N/A","recovered":"N/A","deaths":"N/A"}
    return response

    
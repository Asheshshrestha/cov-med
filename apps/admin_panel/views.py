from django.forms import fields
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,UpdateView,DetailView
from apps.admin_panel.models import WebsiteSettingModel
from apps.admin_panel.forms import WebsiteSettingForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
import requests
import json

class GIndex(LoginRequiredMixin,TemplateView):

    template_name = 'admin/c-panel/pages/index/index.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'index' 
        context["page_name"] = 'Dashboard' 
        context["corona_summary"] = get_coronacasesummary()
        return context

class GDetailSetting(DetailView):
    template_name = 'admin/c-panel/pages/settings/sitesetting.html'
    def get_object(self):
        return WebsiteSettingModel.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'settings' 
        context["page_name"] = 'Website Setting' 
        return context

class GUpdateSetting(SuccessMessageMixin,UpdateView):
    model = WebsiteSettingModel
    form_class = WebsiteSettingForm
    template_name = 'admin/c-panel/pages/settings/update_setting.html'
    success_message = "Page Setting Updated Successfully."
    

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

    
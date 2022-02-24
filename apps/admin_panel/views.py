from django.forms import fields
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView,UpdateView,DetailView
from apps.admin_panel.models import WebsiteSettingModel
from apps.admin_panel.forms import WebsiteSettingForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class GIndex(LoginRequiredMixin,TemplateView):

    template_name = 'admin/c-panel/pages/index/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'index' 
        return context

class GDetailSetting(DetailView):
    template_name = 'admin/c-panel/pages/settings/sitesetting.html'
    def get_object(self):
        return WebsiteSettingModel.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'settings' 
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
    
    
    
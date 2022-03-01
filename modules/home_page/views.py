from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls.base import reverse_lazy
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from apps.admin_panel.models import WebsiteSettingModel
from apps.services.forms import HospitalServiceModuleForm
from apps.services.models import HospitalServiceModule
from apps.accounts.models import BasicUserProfile
# Create your views here.

# Create your views here.
class HomeIndex(TemplateView):

    template_name = 'frontend/pages/homepage/index.html'
    
    def get_context_data(self, **kwargs):
        
        doctors = BasicUserProfile.objects.filter(is_doctor = True)
        context = super().get_context_data(**kwargs)
        context["doctors"] = doctors
        return context
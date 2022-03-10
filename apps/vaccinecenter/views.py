from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls.base import reverse_lazy
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import requests
import json

from apps.vaccinecenter.models import CoronaVaccineCenter
from apps.vaccinecenter.forms import CoronaVaccineCenterFrom
from gronckle_enginee import settings
# Create your views here.
class CoronaVaccineCenterIndex(LoginRequiredMixin,PermissionRequiredMixin,ListView):

    template_name = 'admin/c-panel/pages/coronavaccinecenter/index.html'
    model = CoronaVaccineCenter
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
         
    def get_queryset(self,*args,**kwargs):

        qs = super(CoronaVaccineCenterIndex,self).get_queryset(*args,**kwargs)
        qs = qs.order_by("-id")
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'covidcare' 
        context["page_name"] = 'Vaccine Center Services' 
        return context

class AddCoronaVaccineCenter(SuccessMessageMixin,PermissionRequiredMixin,CreateView):
    form_class = CoronaVaccineCenterFrom
    success_url = reverse_lazy('vaccinecenter_index')
    template_name = 'admin/c-panel/pages/coronavaccinecenter/manage.html'
    success_message = "Vaccine Center Added Successfully ."
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'covidcare' 
        context["page_name"] = 'Vaccine Center Services' 
        return context

class UpdateCoronaVaccineCenter(SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
    model = CoronaVaccineCenter
    form_class = CoronaVaccineCenterFrom
    template_name = 'admin/c-panel/pages/coronavaccinecenter/manage.html'
    success_message = "Vaccine Center Updated Successfully."
    pk_url_kwarg = 'pk'

    success_url = reverse_lazy('vaccinecenter_index')
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'covidcare' 
        context["page_name"] = 'Vaccine Center Services' 
        return context

class DeleteCoronaVaccineCenter(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'admin/c-panel/pages/coronavaccinecenter/delete.html'
    success_message = "Vaccine Center Delete Successfully."
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('vaccinecenter_index')
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
         
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(CoronaVaccineCenter,id=id_)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'covidcare' 
        context["page_name"] = 'Vaccine Center Services' 
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteCoronaVaccineCenter, self).delete(request, *args, **kwargs)

class CovidStatusIndex(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):

    template_name = 'admin/c-panel/pages/coronacase/index.html'
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_staff
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'covidcare' 
        context["page_name"] = 'Covid Case Today' 
        context["cases"] = self.get_corona_case_today()
        return context
    
    def get_corona_case_today(self):
        url = "https://corona.askbhunte.com/api/v1/data/world"
        try:
            payload={}
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            cases = json.loads(response.text)[1:]
        except:
            cases = []
        
        return cases


from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls.base import reverse_lazy
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from apps.hospital.models import HospitalModel
from apps.hospital.forms import HospitalModelForm

class HospitalIndex(LoginRequiredMixin,ListView):

    template_name = 'admin/c-panel/pages/hospital/index.html'
    model = HospitalModel
    def get_queryset(self,*args,**kwargs):

        qs = super(HospitalIndex,self).get_queryset(*args,**kwargs)
        qs = qs.order_by("-id")
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Management' 
        return context

class AddHospital(SuccessMessageMixin,CreateView):
    form_class = HospitalModelForm
    success_url = reverse_lazy('hospital_index')
    template_name = 'admin/c-panel/pages/hospital/manage.html'
    success_message = "Hospital Created Successfully."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Management' 
        return context

class UpdateHospital(SuccessMessageMixin,UpdateView):
    model = HospitalModel
    form_class = HospitalModelForm
    template_name = 'admin/c-panel/pages/hospital/manage.html'
    success_message = "Hospital Updated Successfully."
    pk_url_kwarg = 'pk'

    success_url = reverse_lazy('hospital_index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Management' 
        return context

class DeleteHospital(SuccessMessageMixin,DeleteView):
    template_name = 'admin/c-panel/pages/hospital/delete.html'
    success_message = "Hospital Delete Successfully."
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('hospital_index')
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(HospitalModel,id=id_)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Management' 
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteHospital, self).delete(request, *args, **kwargs)
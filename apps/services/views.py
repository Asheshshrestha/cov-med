from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls.base import reverse_lazy
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from gronckle_enginee import settings

from apps.services.forms import HospitalServiceModuleForm
from apps.services.models import HospitalServiceModule
# Create your views here.


class ServiceIndex(LoginRequiredMixin,PermissionRequiredMixin,ListView):

    template_name = 'admin/c-panel/pages/services/index.html'
    model = HospitalServiceModule
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser

    def get_queryset(self,*args,**kwargs):

        qs = super(ServiceIndex,self).get_queryset(*args,**kwargs)
        qs = qs.order_by("-id")
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Services' 
        return context


class AddHospitalService(PermissionRequiredMixin,CreateView):
    form_class = HospitalServiceModuleForm
    success_url = reverse_lazy('service_index')
    template_name = 'admin/c-panel/pages/services/manage.html'
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Services' 
        return context


class UpdateHospitalService(SuccessMessageMixin,PermissionRequiredMixin,UpdateView):
    model = HospitalServiceModule
    form_class = HospitalServiceModuleForm
    template_name = 'admin/c-panel/pages/services/manage.html'
    success_message = "Services Updated Successfully."
    pk_url_kwarg = 'pk'

    success_url = reverse_lazy('service_index')
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Services' 
        return context

class DeleteHospitalService(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    template_name = 'admin/c-panel/pages/services/delete.html'
    success_message = "Services Delete Successfully."
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('service_index')
    login_url = settings.LOGIN_URL

    def has_permission(self):
         return self.request.user.is_superuser
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(HospitalServiceModule,id=id_)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Hospital Services' 
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteHospitalService, self).delete(request, *args, **kwargs)
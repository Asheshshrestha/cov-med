from urllib import request
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View
from apps.appointment.forms import AppointmentModelForm
from apps.accounts.models import BasicUserProfile
from apps.appointment.models import AppointmentModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime #important if using timezones
from django.db.models import Q

# Create your views here.

class AddAppointment(LoginRequiredMixin,View):

    template_name = 'frontend/pages/appointment/appointment.html'
    
    def get(self,request,pk,*args,**kwargs):
        doctor = BasicUserProfile.objects.get(id=pk)
        doctor_name = 'Dr. '+ doctor.first_name+' '+doctor.last_name
        
        form = AppointmentModelForm()
        return render(request,self.template_name,{'form':form,'doctor_name':doctor_name})
    def post(self,request,pk):
        
        form = AppointmentModelForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.reffer_user = request.user
            appointment.reffer_doctor = BasicUserProfile.objects.get(id=pk).reffer_user
            appointment.save()

            messages.success(request,'Successfully get appointment.')
            return redirect('index_home')
        else:
            messages.warning(request,'Cannont get appointment now, Please try again.')
            return render(request,self.template_name,{'form':form})

class AppointmentListView(ListView):
    template_name = 'admin/c-panel/pages/appointment/index.html'

    model = AppointmentModel
    def get_queryset(self,*args,**kwargs):

        qs = super(AppointmentListView,self).get_queryset(*args,**kwargs)
        qs = qs.order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Appointment Management' 
        context["today"] = datetime.today()
        return context

class DoctorAppointmentListView(ListView):
    template_name = 'admin/c-panel/pages/appointment/myappointmentlist.html'

    model = AppointmentModel
    def get_queryset(self,*args,**kwargs):

        qs = super(DoctorAppointmentListView,self).get_queryset(*args,**kwargs)
        qs = qs.filter(reffer_doctor__id=self.request.user.id).order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Appointment Management' 
        context["today"] = datetime.today()
        return context
class MyAppointmentListView(ListView):
    template_name = 'frontend/pages/appointment/myappointmentlist.html'

    model = AppointmentModel
    def get_queryset(self,*args,**kwargs):
        current_datetime = datetime.datetime.today()
        qs = super(MyAppointmentListView,self).get_queryset(*args,**kwargs)
        qs = qs.filter(Q(reffer_user__id =self. request.user.id) & Q(appointment_date__gte = current_datetime)).order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class AppointmentDetailView(DetailView):
    template_name = 'admin/c-panel/pages/appointment/detail.html'
    model = AppointmentModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'medcore' 
        context["page_name"] = 'Appointment Management' 
        
        return context
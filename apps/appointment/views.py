from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View
from apps.appointment.forms import AppointmentModelForm
from apps.accounts.models import BasicUserProfile
# Create your views here.

class AddAppointment(View):

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
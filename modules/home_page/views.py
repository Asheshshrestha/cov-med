from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls.base import reverse_lazy
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse

import requests
import json
from django.forms.models import model_to_dict

from apps.admin_panel.models import WebsiteSettingModel
from apps.services.forms import HospitalServiceModuleForm
from apps.services.models import HospitalServiceModule
from apps.accounts.models import BasicUserProfile
from apps.vaccinecenter.models import CoronaVaccineCenter
from apps.hospital.models import HospitalModel
from django.db.models import Q

import datetime
# Create your views here.

# Create your views here.
class HomeIndex(TemplateView):

    template_name = 'frontend/pages/homepage/index.html'
    
    def get_context_data(self, **kwargs):
        current_datetime = datetime.datetime.today()
        print(current_datetime)
        doctors = BasicUserProfile.objects.filter(is_doctor = True)
        centers = CoronaVaccineCenter.objects.filter(Q(provide_to__gte=current_datetime))
        hospitals = HospitalModel.objects.filter(in_service=True)
        services = HospitalServiceModule.objects.filter(is_ineffect = True)[:6]
        context = super().get_context_data(**kwargs)
        context["doctors"] = doctors
        context['centers'] = centers
        context['hospitals'] = hospitals
        context["cases"] = self.get_corona_case_today()
        context['services'] = services
        return context
    def get_corona_case_today(self):
        url = "https://corona.askbhunte.com/api/v1/data/world"
        try:
            payload={}
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            cases = json.loads(response.text)[1:20]
        except:
            cases = []
        
        return cases

class CoronaCasesIndex(TemplateView):
    template_name = 'frontend/pages/corona_stats/country_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

def AllServicesView(request):
    if request.method == 'GET':
        services = HospitalServiceModule.objects.filter(is_ineffect = True).values()
        return JsonResponse({'data':list(services)})
    else:
        return JsonResponse({'error':'Unknown error occured'},mimetype='application/json')

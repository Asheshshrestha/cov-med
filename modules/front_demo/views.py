from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class GFrontIndex(TemplateView):

    template_name = 'frontend/index.html'
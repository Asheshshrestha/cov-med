from os import name
from django.urls import path
from django.urls.conf import include
from modules.home_page.views import HomeIndex,CoronaCasesIndex,AllServicesView
from apps.hospital.views import HospitalDetailWithDoctorView


urlpatterns = [
    path('',HomeIndex.as_view(),name='index_home'),
    path('coronatoday/',CoronaCasesIndex.as_view(),name='coronacases'),
    path('allservices/',AllServicesView,name='all_services'),
    path('<int:pk>/hopital/',HospitalDetailWithDoctorView.as_view(),name='hospital_detail_front'),
    
]

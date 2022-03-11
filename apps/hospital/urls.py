from os import name
from django.urls import path
from django.urls.conf import include

from apps.hospital.views import HospitalIndex,AddHospital,UpdateHospital,DeleteHospital,HospitalDetailWithDoctorView

urlpatterns = [
    path('list/',HospitalIndex.as_view(),name='hospital_index'),
    path('create/',AddHospital.as_view(),name='create_hospital'),
    path('<int:pk>/update/',UpdateHospital.as_view(),name='update_hospital'),
    path('<int:pk>/delete_confirm/',DeleteHospital.as_view(),name='delete_hospital'),
    
    
]
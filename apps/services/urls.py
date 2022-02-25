from os import name
from django.urls import path
from django.urls.conf import include
from apps.services.views import ServiceIndex,AddHospitalService,UpdateHospitalService,DeleteHospitalService


urlpatterns = [
    path('list/',ServiceIndex.as_view(),name='service_index'),
    path('create/',AddHospitalService.as_view(),name='create_service'),
    path('<int:pk>/update/',UpdateHospitalService.as_view(),name='update_services'),
    path('<int:pk>/delete_confirm/',DeleteHospitalService.as_view(),name='delete_services'),
    
]

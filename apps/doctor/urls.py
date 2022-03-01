from os import name
from django.urls import path
from django.urls.conf import include

from apps.doctor.views import DoctorListView,AddDoctor,UpdateDoctor,DeleteDoctor

urlpatterns = [
    path('list/',DoctorListView.as_view(),name='doctor_index'),
    path('create/',AddDoctor.as_view(),name='create_doctor'),
    path('<int:pk>/update/',UpdateDoctor.as_view(),name='update_doctor'),
    path('<int:pk>/delete_confirm/',DeleteDoctor.as_view(),name='delete_doctor'),
    
]
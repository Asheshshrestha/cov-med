from os import name
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from apps.doctor.views import DoctorListView,AddDoctor,UpdateDoctor,DeleteDoctor

urlpatterns = [
    path('list/',DoctorListView.as_view(),name='doctor_index'),
    path('create/',AddDoctor.as_view(),name='create_doctor'),
    path('<int:pk>/update/',UpdateDoctor.as_view(),name='update_doctor'),
    path('<int:pk>/delete_confirm/',DeleteDoctor.as_view(),name='delete_doctor'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
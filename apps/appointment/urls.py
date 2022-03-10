from os import name
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from apps.appointment.views import (AddAppointment,
                                    AppointmentListView,
                                    AppointmentDetailView,
                                    MyAppointmentListView,
                                    DoctorAppointmentListView, AppointmentDetailViewFront,DeleteAppointment)

urlpatterns = [
    path('list/',AppointmentListView.as_view(),name='appointment_index'),
    path('myappointment/',login_required(MyAppointmentListView.as_view()),name='my_appointment'),
    path('doctorappointment/',DoctorAppointmentListView.as_view(),name='doctor_appointment'),
    path('<int:pk>/register_appointment/',AddAppointment.as_view(),name='register_appointment'),
    path('<int:pk>/detail/',AppointmentDetailView.as_view(),name='appointment_detail'),
    path('<int:pk>/detail_front/',AppointmentDetailViewFront.as_view(),name='appointment_detail_front'),
    path('<int:pk>/delete_confirm/',DeleteAppointment.as_view(),name='delete_appointment'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
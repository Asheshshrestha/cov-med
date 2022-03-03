from os import name
from django.urls import path
from django.urls.conf import include
from apps.accounts.views import GLoginView
from apps.admin_panel.views import GIndex,GUpdateSetting,GDetailSetting
from django.contrib.auth.decorators import permission_required



urlpatterns = [
    path('home/',(GIndex.as_view()),name='index'),
    path('settings/',(GDetailSetting.as_view()),name='setting'),
    path('settings/update/',(GUpdateSetting.as_view()),name='update_setting'),
    path('service/',include('apps.services.urls')),
    path('hospital/',include('apps.hospital.urls')),
    path('doctor/',include('apps.doctor.urls')),
    path('corona/',include('apps.vaccinecenter.urls')),
    path('groups/',include('apps.user_groups.urls')),
    
]

from os import name
from django.urls import path
from django.urls.conf import include
from apps.admin_panel.views import GIndex,GUpdateSetting,GDetailSetting
from django.contrib.auth.decorators import permission_required



urlpatterns = [
    path('home/',(permission_required('is_staff'))(GIndex.as_view()),name='index'),
    path('settings/',(permission_required('is_staff'))(GDetailSetting.as_view()),name='setting'),
    path('settings/update/',(permission_required('is_staff'))(GUpdateSetting.as_view()),name='update_setting'),
    path('service/',include('apps.services.urls')),
    path('hospital/',include('apps.hospital.urls')),
    path('groups/',include('apps.user_groups.urls')),
    
]

from os import name
from django.urls import path
from django.urls.conf import include
from apps.admin_panel.views import GIndex,GUpdateSetting,GDetailSetting


urlpatterns = [
    path('home/',GIndex.as_view(),name='index'),
    path('settings/',GDetailSetting.as_view(),name='setting'),
    path('settings/update/',GUpdateSetting.as_view(),name='update_setting')
    
]

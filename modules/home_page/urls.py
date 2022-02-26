from os import name
from django.urls import path
from django.urls.conf import include
from modules.home_page.views import HomeIndex


urlpatterns = [
    path('',HomeIndex.as_view(),name='index_home'),
    
]

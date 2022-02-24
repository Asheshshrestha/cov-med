from django.urls import path
from django.urls.conf import include
from modules.front_demo.views import GFrontIndex

urlpatterns = [
    path('home/',GFrontIndex.as_view(),name='fhome')
]
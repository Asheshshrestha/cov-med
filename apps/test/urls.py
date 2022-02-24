from django.urls import path
from django.urls.conf import include
from apps.test.views import TestListView

urlpatterns = [
  
  path('list/',TestListView.as_view(),name='test_list'),
    
]

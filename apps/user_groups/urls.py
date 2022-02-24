from django.urls import path
from django.urls.conf import include
from apps.user_groups.views import GroupListView,CreateGroupView,GroupUpdateView,GroupDeleteView

urlpatterns = [
  
  path('list/',GroupListView.as_view(),name='group_list'),
  path('create/',CreateGroupView.as_view(),name='create_group'),
  path('<int:pk>/update/',GroupUpdateView.as_view(),name='update_group'),
  path('<int:pk>/delete/',GroupDeleteView.as_view(),name='delete_group')
    
]

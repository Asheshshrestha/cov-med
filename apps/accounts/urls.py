from os import name
from django.urls import path
from django.urls.conf import include
from apps.accounts.views import (GLoginView,
                                   GLogoutView,
                                   GUserListView,
                                   SignUpViewAdmin,
                                   GUpdateUserAdmin,
                                   GDeleteUserConfirmAdmin,GPasswordResetView,GChangePasswordView)


urlpatterns = [
       path('login/',GLoginView.as_view(),name='login'),
       path('logout/',GLogoutView.as_view(),name='logout'),
       path('list/',GUserListView.as_view(),name='user_list'),
       path('register/',SignUpViewAdmin.as_view(),name='user_register'),
       path('<int:pk>/resetpassword/',GPasswordResetView.as_view(),name='user_reset_password'),
       path('changepassword/',GChangePasswordView.as_view(),name='change_password'),
       path('<int:pk>/update/',GUpdateUserAdmin.as_view(),name='update_user'),
       path('<int:pk>/delete/',GDeleteUserConfirmAdmin.as_view(),name='delete_user_confirm'),

]
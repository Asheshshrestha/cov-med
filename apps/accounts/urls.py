from os import name
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from apps.accounts.views import (GLoginView,
                                   GLogoutView,
                                   GUserListView,
                                   SignUpViewAdmin,
                                   GUpdateUserAdmin,
                                   GDeleteUserConfirmAdmin,
                                   GPasswordResetView,
                                   GChangePasswordView,
                                   SignUpViewFront,
                                   ChangePasswordFront)
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView


urlpatterns = [
       path('login/',GLoginView.as_view(),name='login'),
       path('logout/',GLogoutView.as_view(),name='logout'),
       path('list/',(permission_required('is_staff'))(GUserListView.as_view()),name='user_list'),
       path('register/',(permission_required('is_staff'))(SignUpViewAdmin.as_view()),name='user_register'),
       path('signup/',SignUpViewFront.as_view(),name='signup'),
       path('<int:pk>/resetpassword/',(permission_required('is_staff'))(GPasswordResetView.as_view()),name='user_reset_password'),
       path('changepassword/',(permission_required('is_staff'))(GChangePasswordView.as_view()),name='change_password'),
       path('userchangepassword/',login_required(ChangePasswordFront.as_view()),name='change_password_front'),
       path('<int:pk>/update/',(permission_required('is_staff'))(GUpdateUserAdmin.as_view()),name='update_user'),
       path('<int:pk>/delete/',(permission_required('is_staff'))(GDeleteUserConfirmAdmin.as_view()),name='delete_user_confirm'),
       path('password-reset/',
         PasswordResetView.as_view(
             template_name='frontend/pages/forget_password/password_reset.html'
         ),
         name='password_reset'),
       path('password-reset/done/',
              PasswordResetDoneView.as_view(
              template_name='frontend/pages/forget_password/password_reset_done.html'
              ),
              name='password_reset_done'),
       path('password-reset-confirm/<uidb64>/<token>/',
              PasswordResetConfirmView.as_view(
              template_name='frontend/pages/forget_password/password_reset_confirm.html'
              ),
              name='password_reset_confirm'),
       path('password-reset-complete/',
              PasswordResetCompleteView.as_view(
              template_name='frontend/pages/forget_password/password_reset_complete.html'
              ),
              name='password_reset_complete'),

]
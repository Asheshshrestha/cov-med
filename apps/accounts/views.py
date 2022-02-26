from cgitb import reset
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ValidationError
from django.http import request
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from gronckle_enginee import settings
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from apps.accounts.forms import SignupForm,UserUpadteForm,ResetPasswordForm,ChangePasswordDashboardForm,UserSignupForm
from django.contrib.auth.hashers import check_password
from apps.accounts.models import BasicUserProfile
from django.contrib.auth.models import Group


class GLoginView(View):
    template_name = 'admin/accounts/login.html'
    def get(self,request,*args,**kwargs):
        form = AuthenticationForm()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = AuthenticationForm(None,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_staff:
                    return HttpResponseRedirect(settings.STAFF_LOGIN_REDIRECT_URL)
                else:
                    return HttpResponseRedirect(settings.USER_LOGIN_REDIRECT_URL)
            else:
                messages.warning(request,'Sorry can\'t login please try again later')
                return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            return render(request,self.template_name,{'form':form})

class GPasswordResetView(View):
    template_name = 'admin/c-panel/pages/user_management/users/user_reset_password.html'
    def get(self,request,*args,**kwargs):
        form = ResetPasswordForm()
        return render(request,self.template_name,{'form':form,'nav_link':'users'})
    def post(self, request,pk):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            password1 =  form.cleaned_data.get('password')
            password2 =  form.cleaned_data.get('confirm_password')
            if password1 == password2:
                user = User.objects.get(id=pk)
                user.set_password(password1)
                user.save()
                messages.success(request,'Successfully reset password')
                return redirect('user_list')
            else:
                form = ResetPasswordForm()
                messages.warning(request,'Password and Confirm Password must be same')
                return render(request,self.template_name,{'form':form,'nav_link':'users'})
            
        else:
            form = ResetPasswordForm()
            messages.warning(request,'Sorry can\'t change password please try again later')
            return render(request,self.template_name,{'form':form,'nav_link':'users'})
            
class GChangePasswordView(View):
    template_name = 'admin/c-panel/pages/user_management/users/change_password.html'
    def get(self,request,*args,**kwargs):
        form = ChangePasswordDashboardForm()
        return render(request,self.template_name,{'form':form,'nav_link':'users'})
    def post(self, request):
        form = ChangePasswordDashboardForm(request.POST)
        currentpassword= request.user.password 
        if form.is_valid():
            currentpasswordentered= form.cleaned_data.get("current_password")
            password1 =  form.cleaned_data.get('password')
            password2 =  form.cleaned_data.get('confirm_password')
            matchcheck= check_password(currentpasswordentered, currentpassword)
            if matchcheck:

                if password1 == password2:
                    user = User.objects.get(id=request.user.id)
                    user.set_password(password1)
                    user.save()
                    messages.success(request,'Successfully change password')
                    return redirect('index')
                else:
                    form = ChangePasswordDashboardForm()
                    messages.warning(request,'Password and Confirm Password must be same')
                    return render(request,self.template_name,{'form':form,'nav_link':'users'})
            else:
                form = ResetPasswordForm()
                messages.warning(request,'Password you entered doesnot match to your previous password.')
                return render(request,self.template_name,{'form':form,'nav_link':'users'})
            
        else:
            form = ResetPasswordForm()
            messages.warning(request,'Sorry can\'t change password please try again later')
            return render(request,self.template_name,{'form':form,'nav_link':'users'})

class ChangePasswordFront(View):
    template_name = 'frontend/pages/change_password/change_password.html'
    def get(self,request,*args,**kwargs):
        form = ChangePasswordDashboardForm()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = ChangePasswordDashboardForm(request.POST)
        currentpassword= request.user.password 
        if form.is_valid():
            currentpasswordentered= form.cleaned_data.get("current_password")
            password1 =  form.cleaned_data.get('password')
            password2 =  form.cleaned_data.get('confirm_password')
            matchcheck= check_password(currentpasswordentered, currentpassword)
            if matchcheck:

                if password1 == password2:
                    user = User.objects.get(id=request.user.id)
                    user.set_password(password1)
                    user.save()
                    messages.success(request,'Successfully change password')
                    return redirect('index')
                else:
                    form = ChangePasswordDashboardForm()
                    messages.warning(request,'Password and Confirm Password must be same')
                    return render(request,self.template_name,{'form':form})
            else:
                form = ChangePasswordDashboardForm()
                messages.warning(request,'Password you entered doesnot match to your previous password.')
                return render(request,self.template_name,{'form':form})
            
        else:
            form = ChangePasswordDashboardForm()
            messages.warning(request,'Sorry can\'t change password please try again later')
            return render(request,self.template_name,{'form':form})

class GLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request,'Successfully logout')
        return HttpResponseRedirect(settings.LOGIN_URL)

class GUserListView(ListView):
    template_name = 'admin/c-panel/pages/user_management/users/user_list.html'

    model = User
    def get_queryset(self,*args,**kwargs):

        qs = super(GUserListView,self).get_queryset(*args,**kwargs)
        qs = qs.filter(is_active=True).order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context

class SignUpViewAdmin(CreateView):

    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'admin/c-panel/pages/user_management/users/user_add.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context
class SignUpViewFront(View):

    template_name = 'frontend/pages/signup/user_signup.html'

    def get(self,request,*args,**kwargs):
        form = UserSignupForm()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            email =  form.cleaned_data.get('email')
            username =  form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')
            password_confirm =  form.cleaned_data.get('password_confirm')
            first_name =  form.cleaned_data.get('first_name')
            last_name =  form.cleaned_data.get('last_name')
            age =  form.cleaned_data.get('age')
            dateofbirth =  form.cleaned_data.get('dateofbirth')
            gender =  form.cleaned_data.get('gender')
            if password == password_confirm:
                new_user = User.objects.create_user(username, email, password)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                user_group = Group.objects.get(name='User') 
                user_group.user_set.add(new_user)

                user_profile = BasicUserProfile(age=age,dateofbirth= dateofbirth,gender=gender,user = new_user)
                user_profile.save()
                messages.success(request,'Successfully created your account.')
                return HttpResponseRedirect(settings.LOGIN_URL)
            else:
                messages.warning(request,'Password must match to each other.')
                return render(request,self.template_name,{'form':form})
            
        else:
            print('what the heck')
            messages.warning(request,'Sorry cannot signup now please try again later.')
            return render(request,self.template_name,{'form':form})

class GUpdateUserAdmin(SuccessMessageMixin,UpdateView):
    model = User
    form_class = UserUpadteForm
    template_name = 'admin/c-panel/pages/user_management/users/user_update.html'
    success_message = "User Profile Updated Successfully."
    pk_url_kwarg = 'pk'

    def get_success_url(self, *args, **kwargs):
        return '/accounts/list/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context



class GDeleteUserConfirmAdmin(SuccessMessageMixin,DeleteView):

    template_name = 'admin/c-panel/pages/user_management/users/delete_user.html'
    success_message = "User Delete Successfully."
    pk_url_kwarg = 'pk'

    def get_success_url(self, *args, **kwargs):
        return '/accounts/list/'
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(User,id=id_)
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(GDeleteUserConfirmAdmin, self).delete(request, *args, **kwargs)


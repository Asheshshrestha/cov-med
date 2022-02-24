from django.contrib import messages
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.utils.functional import lazy
from apps.user_groups.forms import GroupCreateForm
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView



class CreateGroupView(SuccessMessageMixin,CreateView):

    form_class = GroupCreateForm
    success_url = reverse_lazy('group_list')
    success_message = "User Group created Successfully."
    template_name = 'admin/c-panel/pages/user_management/roles/group_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context

class GroupListView(ListView):

    model = Group
    template_name = 'admin/c-panel/pages/user_management/roles/group_list.html'

    def get_queryset(self,*args,**kwargs):

        qs = super(GroupListView,self).get_queryset(*args,**kwargs)
        qs = qs.order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context


class GroupUpdateView(SuccessMessageMixin,UpdateView):

    model = Group 
    form_class = GroupCreateForm
    template_name = 'admin/c-panel/pages/user_management/roles/group_update.html'
    success_message = "User Group Updated Successfully."
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('group_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context

class GroupDeleteView(SuccessMessageMixin,DeleteView):

    model = Group
    template_name = 'admin/c-panel/pages/user_management/roles/delete_group.html'
    success_message = 'Group Deleted Successfully'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('group_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'users' 
        return context

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(GroupDeleteView, self).delete(request, *args, **kwargs)
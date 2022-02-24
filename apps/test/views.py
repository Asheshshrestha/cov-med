from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.functional import lazy
from django.views.generic.edit import CreateView
from apps.test.forms import TestCreateForm
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from apps.test.models import TestModel
# Create your views here.

class CrateTestView(SuccessMessageMixin,CreateView):
    form_class = TestCreateForm
    success_url = reverse_lazy('group_list')
    success_message = "successfully created test object"
    template_name = ""


class TestListView(SuccessMessageMixin,ListView):

    model = TestModel
    template_name = 'admin/test/test_list.html'

    def get_queryset(self, *args, **kwargs):

        qs = super(TestListView,self).get_queryset( *args, **kwargs)
        qs = qs.order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nav_link"] = 'test'
        return context
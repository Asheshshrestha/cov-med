from django.contrib import admin

# Register your models here.
from apps.test.models import TestModel

admin.site.register(TestModel)

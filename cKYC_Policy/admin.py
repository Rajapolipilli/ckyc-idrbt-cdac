from django.contrib import admin
from .models import Policy,PolicyField
# Register your models here.

admin.site.register(Policy)
admin.site.register(PolicyField)
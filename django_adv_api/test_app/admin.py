from django.contrib import admin
from .models import TestModel,ModelX,ModelY

admin.site.register((TestModel,ModelX,ModelY))

# Register your models here.

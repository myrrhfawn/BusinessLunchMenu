from django.contrib import admin

# Register your models here.
from .models import Menu, Order

admin.site.register(Menu)
admin.site.register(Order)
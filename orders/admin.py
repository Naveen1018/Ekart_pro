from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.

@register(order_model)
class orderAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'account', 'first_name', 'last_name', 'phone', 'email', 'country', 'state', 'street', 'building', 'house', 'postal', 'cardno', 'expiry', 'cvv', 'amount', 'orderdate']

@register(order_items)
class itemAdmin(admin.ModelAdmin):
    list_display = ['inv', 'product', 'image']
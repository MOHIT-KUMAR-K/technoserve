from django.contrib import admin

# Register your models here.

from .models import Item,Order, OrderItem

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
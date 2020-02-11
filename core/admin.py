from django.contrib import admin

from .models import Item, orderItem, Order

admin.site.register(Item)
admin.site.register(orderItem)
admin.site.register(Order)

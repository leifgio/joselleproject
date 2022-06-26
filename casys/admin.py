from django.contrib import admin

from .models import Client, Order, Product, Shipment, Product_Receive

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Shipment)
admin.site.register(Product_Receive)

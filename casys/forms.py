from django.forms import ModelForm
from .models import *
from django import forms

class CreateClient(ModelForm):
    class Meta:
        model = Client
        fields = ['firstname', 'surname', 'contact_number', 'address']

# admin page
class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'art_medium', 'size', 'price', 'quantity']

class CreateOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['user_information', 'product_name', 'reference_picture', 'courier', 'gcash_number', 'gcash_name', 'proof_of_payment']
        
class CreateShipment(ModelForm):
    class Meta:
        model = Shipment
        fields = ['order_name', 'date_to_ship', 'time_to_ship']

class CreateReceived(ModelForm):
    class Meta:
        model = Product_Receive
        fields = ['recipient_name', 'proof_received', 'feedback']

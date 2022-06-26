from django.shortcuts import render,redirect
from .models import Client, Order, Shipment, Product_Receive, Product

from django.views import generic
from django.http import Http404, HttpResponse
from casys.forms import CreateClient, CreateProduct, CreateOrder, CreateShipment, CreateReceived

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def MainPage(request):
	return render(request, 'mainpage.html')

def OrderView(request):
    order = Order.objects.all()
    queries = {'order': order}
    return render(request, "orders.html", queries)

def ClientView(request):
    client = Client.objects.all()
    queries = {'client': client}
    return render(request, "client.html", queries)

class OrderSummaryView(generic.DetailView):
    model = Order
    template_name = 'order-summary.html'

def ProductView(request):
    product = Product.objects.all()
    queries = {'product': product}
    return render(request, "products.html", queries)

def ShipmentView(request):
    shipment = Shipment.objects.all()
    queries = {'shipment': shipment}
    return render(request, "shipments.html", queries)

def AddClient(request):
    form = CreateClient()
    if request.method == 'POST':
        client = CreateClient(request.POST)
        if client.is_valid():
            client.save()
    value = {'form':form}
    return render(request, 'create.html',value)

def AddOrder(request):
    form = CreateOrder()
    if request.method == 'POST':
        order = CreateOrder(request.POST)
        if order.is_valid():
            order.save()
    value = {'form':form}
    return render(request, 'create.html',value)

def AddShipment(request):
    form = CreateShipment()
    if request.method == 'POST':
        shipment = CreateShipment(request.POST)
        if shipment.is_valid():
            shipment.save()
    value = {'form':form}
    return render(request, 'create.html',value)

def AddReceived(request):
    form = CreateReceived()
    if request.method == 'POST':
        received = CreateReceived(request.POST)
        if received.is_valid():
            received.save()
    value = {'form':form}
    return render(request, 'create.html',value)

@login_required(login_url='casys:login')
def AddProduct(request):
    form = CreateProduct()
    if request.method == 'POST':
        product = CreateProduct(request.POST)
        if product.is_valid():
            product.save()
    value = {'form':form}
    return render(request, 'create.html',value)

def loginPage(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('Password')

        user = authenticate(request, username = un, password =pw)

        if user is not None:
            login(request, user)
            return redirect('casys:products')
    return render(request, "login.html")

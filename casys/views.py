from django.shortcuts import get_object_or_404,render,redirect
from django.utils import timezone
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

def ProductView(request):
    product = Product.objects.all()
    queries = {'product': product}
    return render(request, "products.html", queries)

def ShipmentView(request):
    shipment = Shipment.objects.all()
    queries = {'shipment': shipment}
    return render(request, "shipments.html", queries)

class FeedbackDetail(generic.DetailView):
    model = Product_Receive
    template_name = 'feedback-detail.html'

def FeedbackView(request):
    feedback = Product_Receive.objects.all()
    queries = {'feedback': feedback}
    return render(request, "feedback.html", queries)

def AddClient(request):
    form = CreateClient()
    if request.method == 'POST':
        client = CreateClient(request.POST)
        if client.is_valid():
            client.save()
            return redirect('casys:client')
    value = {'form':form}
    return render(request, 'create.html',value)

def AddOrder(request):
    form = CreateOrder()
    if request.method == 'POST':
        order = CreateOrder(request.POST)
        if order.is_valid():
            order.save()
            return redirect('casys:order')
    value = {'form':form}
    return render(request, 'create.html',value)

def AddShipment(request):
    form = CreateShipment()
    if request.method == 'POST':
        shipment = CreateShipment(request.POST)
        if shipment.is_valid():
            shipment.save()
            return redirect('casys:order')
    value = {'form':form}
    return render(request, 'create.html',value)

def AddReceived(request):
    form = CreateReceived()
    if request.method == 'POST':
        received = CreateReceived(request.POST, request.FILES)
        if received.is_valid():
            received.save()
            return redirect('casys:feedback')
    value = {'form':form}
    return render(request, 'create.html',value)

@login_required(login_url='casys:login')
def AddProduct(request):
    form = CreateProduct()
    if request.method == 'POST':
        product = CreateProduct(request.POST)
        if product.is_valid():
            product.save()
            return redirect('casys:products')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateClient(request,pk):
    updateditem = Client.objects.get(id=pk)
    form = CreateClient(instance=updateditem)
    if request.method == "POST":
        client = CreateClient(request.POST,instance=updateditem)
        if client.is_valid:
            client.save()
            return redirect('casys:client')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteClient(request,pk):
    deleteclient = Client.objects.get(id=pk)
    if request.method == "POST":
        deleteclient.delete()
        return redirect('casys:client')
    value = {'item':deleteclient}
    return render(request, 'create.html',value)

def DeleteOrder(request,pk):
    deleteorder = Order.objects.get(id=pk)
    if request.method == "POST":
        deleteorder.delete()
        return redirect('casys:order')
    value = {'item':deleteorder}
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

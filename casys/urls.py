from . import views
from django.urls import path, include

app_name = 'casys'
urlpatterns = [
    path('products/', views.ProductView, name="products"),
    path('create-client/', views.AddClient, name="create-client"),
    path('create-product/', views.AddProduct, name="create-product"),
    path('create-order/', views.AddOrder, name="create-order"),
    path('create-shipment/', views.AddShipment, name="create-shipment"),
    path('create-received/', views.AddReceived, name="create-received"),

    path('client/', views.OrderView, name="order"),
    path('', views.ClientView, name="client"),
    path('orders/<int:pk>/', views.OrderSummaryView.as_view(), name='order-summary'),

    path('login/', views.loginPage, name='login'),
]


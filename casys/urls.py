from . import views
from django.urls import path, include

app_name = 'casys'
urlpatterns = [
    path('create-client/', views.AddClient, name="create-client"),
    path('create-product/', views.AddProduct, name="create-product"),
    path('create-order/', views.AddOrder, name="create-order"),
    path('create-shipment/', views.AddShipment, name="create-shipment"),
    path('create-received/', views.AddReceived, name="create-received"),

    path('update-client/<str:pk>/', views.UpdateClient, name="update-client"),

    path('delete-client/<str:pk>/', views.DeleteClient, name="delete-client"),
    path('delete-order/<str:pk>/', views.DeleteOrder, name="delete-order"),

    path('order/', views.OrderView, name="order"),
    path('products/', views.ProductView, name="products"),
    path('feedback/', views.FeedbackView, name="feedback"),
    path('feedback/<int:pk>/', views.FeedbackDetail.as_view(), name='feedback-detail'),
    path('', views.ClientView, name="client"),

    path('login/', views.loginPage, name='login'),
]


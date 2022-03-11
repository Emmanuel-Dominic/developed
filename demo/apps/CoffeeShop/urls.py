from django.urls import path
from . import views

app_name = "coffee"
urlpatterns = [
    path('store/', views.OrderStore, name='store'),
    path('order/', views.PlaceOrder, name='order'),
]

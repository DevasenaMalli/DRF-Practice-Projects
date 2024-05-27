from django.shortcuts import render

# Create your views here.
from .models import Order,Customer
from nsaApp.serializers import OrderSerializer,CustomerSerializer
from rest_framework import generics

# Create your views here.

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Customer.objects.all()
    serializer_class = CustomerSerializer

from django.shortcuts import render
from .models import OrderItem
from .serializers import OrderItemSerializer,OrderCreateSerializer,OrderItemCreateSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
# Create your views here.

class OrderItemView(ListAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class OrderCreateView(CreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderCreateSerializer

class OrderUpdateView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderCreateSerializer



class OrderItemCreateView(CreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemCreateSerializer

class OrderItemUpdateView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
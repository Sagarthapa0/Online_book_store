from django.shortcuts import render
from .models import OrderItem
from .serializers import OrderSerializer,OrderItemSerializer,OrderCreateSerializer,OrderItemCreateSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
# Create your views here.

class OrderView(ListAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderSerializer

class OrderCreateView(CreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderCreateSerializer

class OrderUpdateView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderSerializer

class OrderDeleteView(DestroyAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderSerializer



class OrderItemListView(ListAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer


class OrderItemCreateView(CreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemCreateSerializer


class OrderItemUpdateView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer


class OrderItemRetrieveView(RetrieveAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer


class OrderItemDeleteView(DestroyAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer



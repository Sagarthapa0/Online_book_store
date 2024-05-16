
from django.shortcuts import render
from rest_framework import generics, status,permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer,AddToCartSerializer,CartItemCreateSerializer
from books.models import BookOption, Book


class CartView(generics.ListAPIView):
    queryset=Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    

class CartItemListView(generics.ListAPIView):
    serializer_class=CartItemSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        cart=Cart.objects.get(user=user)
        return CartItem.objects.filter(cart=cart)


# class CartItemDetailView(generics.ListAPIView):
#     serializer_class = CartItemSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return CartItem.objects.filter(cart__user=self.request.user)


class CartItemCreateView(generics.CreateAPIView):
    queryset=CartItem.objects.all()
    serializer_class = CartItemCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
    
class CartItemUpdateView(generics.UpdateAPIView):
    serializer_class = CartItemCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class CartItemRetrieveView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class CartItemDeleteView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)




class AddToCartView(generics.CreateAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart_item = serializer.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, CartItemCreateSerializer
from books.models import BookOption, Book


class CartView(generics.RetrieveAPIView):
    queryset=Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [IsAuthenticated]

    # def get(self,request,*args, **kwargs):
    #     user = self.request.data['user']
    #     cart, created = Cart.objects.get_or_create(user=user)
    #     return cart

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItemCreateSerializer
    
    # permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     cart, created = Cart.objects.get_or_create(user=request.user)
    #     data = {
    #         'cart_id':cart.id,
    #         'book' : request.data.get('book'),
    #         'quantity' : int(request.data.get('quantity', 1)),
    #         'order_option' : request.data.get('order_option')
    #     }
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

        # print(f'qu: {quantity}, car: {cart}, bo: {book}, or: {order_option}')

        # return Response({'message': 'IM HERE'})

        # Check if the book exists
        # try:
        #     book = Book.objects.get(id=book)
        # except Book.DoesNotExist:
        #     return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # if not BookOption.objects.filter(id=order_option).exists():
        #     return Response({"error": "Invalid order option."}, status=status.HTTP_400_BAD_REQUEST)
        
        # if book.quantity < quantity:
        #     return Response({"error": "Not enough quantity available."}, status=status.HTTP_400_BAD_REQUEST)

        # cart_item, created = CartItem.objects.get_or_create(cart=cart, book_id=book, order_option_id=order_option, defaults={'quantity': quantity})
        # if not created:
        #     if book.quantity < cart_item.quantity + quantity:
        #         return Response({"error": "Not enough quantity available."}, status=status.HTTP_400_BAD_REQUEST)
        #     cart_item.quantity += quantity
        #     cart_item.save()
        
        # # Decrease the book quantity
        # book.quantity -= quantity
        # book.save()

        # return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)


class UpdateCartItemView(generics.UpdateAPIView):
    queryset=CartItem.objects.all()
    serializer_class = CartItemSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

class RemoveFromCartView(generics.DestroyAPIView):
    queryset=CartItem.objects.all()
    serializer_class = CartItemSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
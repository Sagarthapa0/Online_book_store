from rest_framework import serializers
from .models import Cart, CartItem
from books.models import BookOption,Book

class CartItemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    order_option = serializers.PrimaryKeyRelatedField(queryset=BookOption.objects.all())

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity', 'order_option']

    def create(self, validated_data):
        cart_id = validated_data.get('cart_id',None)
        book = validated_data.get('book',None)
        quantity = validated_data.get('quantity',None)
        order_option = validated_data.get('order_option',None)

        return CartItem.objects.create(

        )

class CartItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'quantity', 'order_option']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at', 'updated_at']


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        # fields = '__all__'
        fields = ['book', 'quantity', 'order_option']

    def create(self, validated_data):
        book = self.validated_data['book'].id
        order_option = self.validated_data['order_option'].id

        books = Book.objects.get(id=book)
        order_option = Book.objects.get(id=order_option)

        # user = self.context['request'].user
        # # check cart if exist else create new
        # cart, created = Cart.objects.get_or_create(user=user)

        # cart.save()
        return books

    # def create(self, validated_data):
    #     book = self.validated_data['book']
    #     print(book)

    #     return book


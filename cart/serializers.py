from rest_framework import serializers
from .models import Cart, CartItem
from books.models import BookOption,Book
from books.serializers import BookSerializer
from django.contrib.auth.models import AnonymousUser
from user.serializers import UserListSerializer



class CartItemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    order_option = serializers.PrimaryKeyRelatedField(queryset=BookOption.objects.all())
    
    # cost=serializers.FloatField()
    book = BookSerializer()

    class Meta:
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    # user = UserListSerializer()
    user = serializers.StringRelatedField()
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at', 'updated_at']


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["book","quantity","order_option"]

    def create(self,validated_data):
        user=self.context['request'].user
        book=self.validated_data["book"].id
        quantity=self.validated_data['quantity']
        order_option=self.validated_data['order_option']

        if isinstance(user,AnonymousUser):
            raise serializers.ValidationError("User must be authenticated ")
        
        cart,created = Cart.objects.get_or_create(user=user)
        cart_item = CartItem.objects.filter(cart=cart,book=book).first()

        book= Book.objects.get(id=book)
        if quantity > book.quantity:
            raise serializers.ValidationError(f"only {book.quantity} items are available in stock for {book.name}")
        
        if cart_item:
            cart_item.quantity = quantity
        else:
            cart_item =  CartItem.objects.create(cart=cart,**validated_data)

        cart_item.save()
        return cart_item
    


class AddToCartSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    quantity = serializers.IntegerField(min_value=1)
    order_option = serializers.PrimaryKeyRelatedField(queryset=BookOption.objects.all())

    def validate(self, data):
        user = self.context['request'].user

        if isinstance(user, AnonymousUser):
            raise serializers.ValidationError("User must be authenticated")

        book = data['book']
        quantity = data['quantity']

        if quantity > book.quantity:
            raise serializers.ValidationError(f"Only {book.quantity} items are available in stock for {book.name}")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        book = validated_data['book']
        quantity = validated_data['quantity']
        order_option = validated_data['order_option']

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, order_option=order_option)

        if not created:
            new_quantity = cart_item.quantity + quantity
            if new_quantity > book.quantity:
                raise serializers.ValidationError(f"Only {book.quantity} items are available in stock for {book.name}")
            cart_item.quantity = new_quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        # Decrease the book quantity
        book.quantity -= quantity
        book.save()

        return cart_item







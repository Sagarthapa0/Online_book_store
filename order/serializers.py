from rest_framework import serializers
from .models import Order,OrderItem,Buy,Rent
from books.models import BookOption
from user.serializers import UserListSerializer,AddressSerializer



class OrderSerializer(serializers.ModelSerializer):
    buyer=UserListSerializer()
    shipping_address=AddressSerializer()
    billing_address=AddressSerializer()
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    buyer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = "__all__"



class OrderItemSerializer(serializers.ModelSerializer):
    order=OrderSerializer()
    item = serializers.StringRelatedField()
    order_option = serializers.StringRelatedField()
    
    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()


    class Meta:
        model=OrderItem
        fields=[ "id","order","item","quantity","price","cost","created_at","updated_at","order_option",]

    
    def get_price(self, obj):
        return obj.item.price

    def get_cost(self, obj):
        return obj.cost
    



class OrderItemCreateSerializer(serializers.ModelSerializer):
    # order = OrderSerializer()
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    # order_option = serializers.PrimaryKeyRelatedField(queryset=BookOption.objects.all())
   
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "item",
            "order",
            "quantity",
            "order_option",
        )

    def create(self, validated_data):
        book = validated_data.get('item', None)
        quantity= validated_data.get("quantity",1)
        order_item = OrderItem.objects.create(**validated_data)
        order_option_instance = validated_data.pop("order_option")

        if book.quantity < quantity:
            raise serializers.ValidationError("Not Enough books available")
        
        book.quantity -= quantity
        book.save()

        if order_option_instance == "Rent":
            rent_data = {
                "renter": self.context["request"].user,
                "book": book,
                "rent_date": validated_data["order"].created_at.date(),  # Assuming rent date is the order creation date
                "return_date": None,  # Set the return date later based on business logic
                "status": Rent.PENDING,  # Set the initial status to pending
            }
            rent = Rent.objects.create(**rent_data)
        else:
            buy_data = {"book": book}
            buy = Buy.objects.create(**buy_data)

        # order_item.order=order
        # order_item.save()
        # order_option.save()
        return order_item

    def update(self, instance, validated_data):
        instance.item = validated_data.get("item", instance.item)
        instance.order_option = validated_data.get("order_option", instance.order_option)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.save()
        return instance







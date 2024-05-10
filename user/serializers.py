from rest_framework import serializers
from .models import User,UserAddress
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    address=AddressSerializer()
    # return_date = serializers.DateField(
    class Meta:
        model = User
        fields = ["username","password","email","seller","address"]

    def create(self,validated_data):
        address_data=validated_data.pop("address")
        address=UserAddress.objects.create(**address_data)
        validated_data["address"] = address

        seller=validated_data.get('seller')        
        user=User.objects.create_user(**validated_data)
        try:
            seller_group = Group.objects.get(name='seller')
            buyer_group = Group.objects.get(name='buyer')
        except Group.DoesNotExist:
            raise serializers.ValidationError('Group not found')
        if seller:
            user.groups.add(seller_group)
        else:
            user.groups.add(buyer_group)

        user.address=address
        user.save()
        return user

# if order+option == return
#     rent.objects.create 
# else
#     buy create 
class UserListSerializer(serializers.ModelSerializer):
    address= AddressSerializer()
    class Meta:
        model = User
        fields=["id","email","username","seller","address"]

    def update(self, instance, validated_data):
        print(validated_data)
        instance.email = validated_data.get('email',instance.email)
        instance.username = validated_data.get('username',instance.username)
        instance.seller = validated_data.get('seller',instance.seller)
        instance.address.country = validated_data.get('address').get('country',instance.address.country)
        instance.address.state = validated_data.get('address')
        instance.address.city = validated_data.get('city',instance.address.city)
        instance.address.zipcode = validated_data.get('zipcode',instance.address.zipcode)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                msg = 'unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg='Must include username and password.'
            raise serializers.ValidationError(msg, code="authorization")
        
        attrs['user']=user
        return attrs
                




class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
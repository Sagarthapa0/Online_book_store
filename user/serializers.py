from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","email","seller"]

    def create(self,validated_data):
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
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["id","email","username","seller"]



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
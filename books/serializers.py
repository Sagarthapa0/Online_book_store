from .models import Book,BookCategory,BookSubCategory,Author,BookOption
from rest_framework import serializers
from user.models import User


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"

class BookSUbCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSubCategory
        fields = "__all__"

class BookOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOption
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"







class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    sub_category = serializers.StringRelatedField()
    author = serializers.StringRelatedField(many=True)
    available_to = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = "__all__"
        


    # def get_seller():
    #     return User.objects.filter(seller=True)
    

class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


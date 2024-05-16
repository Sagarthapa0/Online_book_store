from .models import Book,BookCategory,BookSubCategory,Author,BookOption,Comment
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




class BookListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    sub_category = serializers.StringRelatedField()
    author = serializers.StringRelatedField(many=True)
    available_to = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    comments= serializers.SerializerMethodField()
    # comments = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ["category","sub_category","author","name","description","image","available_to","price","quantity","created_at","updated_at","is_available","seller","comments",]
        

    def get_comments(self,obj):
        comments=Comment.objects.filter(book=obj, is_visible=False)
        return CommentSerializer(comments,many=True).data



class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    sub_category = serializers.StringRelatedField()
    author = serializers.StringRelatedField(many=True)
    available_to = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    # comments= serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    # def get_comments(self,obj):
    #     comments=Comment.objects.filter(book=obj, is_visible=True)
    #     return CommentSerializer(comments,many=True).data

    # def get_seller():
    #     return User.objects.filter(seller=True)
    

class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'

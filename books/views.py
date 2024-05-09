from django.shortcuts import render
from .serializers import BookSerializer,BookCategorySerializer,BookSUbCategorySerializer,AuthorSerializer,BookOptionSerializer,BookCreateSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .models import Book,BookCategory,BookSubCategory,Author,BookOption


class BookCategoryListView(ListAPIView):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer

class BookCategoryRetrieveView(RetrieveAPIView):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer

class BookCategoryCreateView(CreateAPIView):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer

class BookCategoryUpdateView(UpdateAPIView):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer

class BookCategoryDeleteView(DestroyAPIView):
    queryset=BookCategory.objects.all()
    serializer_class=BookCategorySerializer




class BookSubCategoryListview(ListAPIView):
    queryset=BookSubCategory.objects.all()
    serializer_class=BookSUbCategorySerializer

class BookSubCategoryRetrieveview(RetrieveAPIView):
    queryset=BookSubCategory.objects.all()
    serializer_class=BookSUbCategorySerializer

class BookSubCategoryUpdateview(UpdateAPIView):
    queryset=BookSubCategory.objects.all()
    serializer_class=BookSUbCategorySerializer

class BookSubCategoryCreateview(CreateAPIView):
    queryset=BookSubCategory.objects.all()
    serializer_class=BookSUbCategorySerializer

class BookSubCategoryDeleteview(DestroyAPIView):
    queryset=BookSubCategory.objects.all()
    serializer_class=BookSUbCategorySerializer


class AuthorListView(ListAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorRetrieveView(RetrieveAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorCreateView(CreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorUpdateView(UpdateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorDeleteView(DestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer




class BookOptionListView(ListAPIView):
    queryset=BookOption.objects.all()
    serializer_class=BookOptionSerializer

    
class BookOptionCreateView(CreateAPIView):
    queryset=BookOption.objects.all()
    serializer_class=BookOptionSerializer

class BookOptionUpdateView(UpdateAPIView):
    queryset=BookOption.objects.all()
    serializer_class=BookOptionSerializer

class BookOptionRetrieveView(RetrieveAPIView):
    queryset=BookOption.objects.all()
    serializer_class=BookOptionSerializer

class BookOptionDeleteView(DestroyAPIView):
    queryset=BookOption.objects.all()
    serializer_class=BookOptionSerializer








class BookListView(ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookRetrieveView(RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    lookup_field="slug"

class BookCreateView(CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookCreateSerializer

class BookUpdateView(UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDeleteView(DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer



# Create your views here.
class BookBuyRentView(ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def get_queryset(self):
        # sourcery skip: inline-immediately-returned-variable
        book_option=[self.kwargs.get("book_option")]
        option = self.queryset.filter(available_to__can=book_option)
        return option


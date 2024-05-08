from django.contrib import admin
from .models import BookCategory,Book,BookSubCategory,Author,BookOption

# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(BookOption)
admin.site.register(Author)
admin.site.register(BookSubCategory)

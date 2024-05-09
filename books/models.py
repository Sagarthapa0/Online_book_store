from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class BookCategory(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    icon=models.ImageField(upload_to='media', blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Book Category")
        verbose_name_plural = _("Book Categories")

    def __str__(self) -> str:
        return self.name
    
class BookSubCategory(models.Model):
    category=models.ForeignKey(BookCategory,verbose_name=("Book Category"),on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    


class Author(models.Model):
    GENDER_CHOICES=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    name=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return self.name
    
    
class BookOption(models.Model):
    can=models.CharField(max_length=100,blank=False,null=False)

    def __str__(self) -> str:
        return self.can
    


class Book(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True)
    category = models.ForeignKey(BookCategory,verbose_name=("BookCategory"),on_delete=models.CASCADE)
    sub_category=models.ForeignKey(BookSubCategory, verbose_name=("BookSubCategory"),on_delete=models.CASCADE)
    author=models.ManyToManyField(Author, verbose_name=("Authors"))
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='media',blank=True)

    available_to=models.ForeignKey(BookOption,on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available=models.BooleanField(default=False)

    seller=models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    

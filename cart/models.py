from django.db import models
from user.models import User
from books.models import Book,BookOption

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"Cart for {self.user.username}"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_option = models.ForeignKey(BookOption, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cart', 'book', 'order_option')

    def __str__(self):
        return f"CartItem({self.cart.user.username}, {self.book.name}, {self.quantity})"
    

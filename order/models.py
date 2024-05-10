from django.db import models
from books.models import Book,BookOption
from user.models import User,UserAddress
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Order(models.Model):
    PENDING = "P"
    COMPLETED = "C"

    STATUS_CHOICES = ((PENDING, _("pending")), (COMPLETED, _("completed")))

    buyer=models.ForeignKey(User,verbose_name=("Book Buyer"),on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default=PENDING)
    shipping_address=models.ForeignKey(UserAddress,related_name="shipping_orders",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    billing_address = models.ForeignKey(UserAddress,related_name="billing_orders",on_delete=models.SET_NULL,blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.buyer.username
    

class OrderItem(models.Model):
    item=models.ForeignKey(Book,related_name="book_orders", on_delete=models.CASCADE)
    order=models.ForeignKey(Order,related_name="order_items", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_option=models.ForeignKey(BookOption,on_delete=models.CASCADE)

    def __str__(self):
        return self.order.buyer.get_full_name()
    
    @cached_property
    def cost(self):
        """
        Total cost of the ordered item
        """
        return round(self.quantity * self.item.price, 2)






    


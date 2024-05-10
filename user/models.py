from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserAddress(models.Model):
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()

    def __str__(self) -> str:
        return self.city



class User(AbstractUser):
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.BooleanField(default=False)
    address=models.ForeignKey(UserAddress,verbose_name=("User Address"),on_delete=models.SET_NULL,null=True)
    #buyer=models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.username

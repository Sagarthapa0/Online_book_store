from django.urls import path
from .views import CartView, AddToCartView, UpdateCartItemView, RemoveFromCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='cart-add'),
    path('<int:pk>/update/', UpdateCartItemView.as_view(), name='cart-update'),
    path('<int:pk>/remove/', RemoveFromCartView.as_view(), name='cart-remove'),
]

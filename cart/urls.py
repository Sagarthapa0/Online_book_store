from django.urls import path
from .views import CartView,AddToCartView,CartItemListView,CartItemRetrieveView,CartItemCreateView,CartItemUpdateView,CartItemDeleteView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', AddToCartView.as_view(), name='cart-add'),


    path('items/', CartItemListView.as_view(), name='cartitem-list'),
    path('items/<int:pk>/', CartItemRetrieveView.as_view(), name='cartitem-retrieve'),
    path('items/create/', CartItemCreateView.as_view(), name='cartitem-create'),
    path('items/<int:pk>/update/', CartItemUpdateView.as_view(), name='cartitem-update'),
    path('items/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cartitem-delete'),






]

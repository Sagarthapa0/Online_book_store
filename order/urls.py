from django.urls import path
from .views import OrderItemView,OrderItemUpdateView,OrderCreateView,OrderItemCreateView

urlpatterns=[
    path("",OrderItemView.as_view(),name="order-view"),
    path("create/",OrderCreateView.as_view(),name="order-create"),
    path("<int:pk>/update/",OrderItemUpdateView.as_view(),name="order-update"),


    path("orderitem/create/",OrderItemCreateView.as_view(),name="orderitem-create"),

]
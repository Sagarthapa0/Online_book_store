from django.urls import path
from .views import OrderItemListView,OrderItemUpdateView,OrderCreateView,OrderItemCreateView,OrderDeleteView,OrderUpdateView,OrderView,OrderRetrieveView,OrderItemRetrieveView,OrderItemDeleteView


urlpatterns=[
    path("order",OrderView.as_view(),name="order-list"),
    path("order/create/",OrderCreateView.as_view(),name="order-create"),
    path("order/<int:pk>/update/",OrderUpdateView.as_view(),name="order-update"),
    path("order/retrieve/",OrderRetrieveView.as_view(),name="order-retrieve"),
    path("order/<int:pk>/delete/",OrderDeleteView.as_view(),name="order-delete"),


    path("",OrderItemListView.as_view(),name="order-view"),
    path("create/",OrderItemCreateView.as_view(),name="orderitem-create"),
    path("<int:pk>",OrderItemRetrieveView.as_view(),name="orderitem-retrieve"),
    path("<int:pk>/update/",OrderItemUpdateView.as_view(),name="orderitem-update"),
    path("<int:pk>/delete/",OrderItemDeleteView.as_view(),name="orderitem-delete"),

]
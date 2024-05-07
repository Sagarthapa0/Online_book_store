from django.urls import path
from .views import UserCreateView,SellerListView,BuyerListView,UserListView,UserRetrieveView,UserUpdateView,UserDeleteView,UserLoginView,LogoutView

urlpatterns=[
    path("",UserListView.as_view(),name='user-list'),
    path("create/",UserCreateView.as_view(),name='user-create'),
    path("seller/",SellerListView.as_view(),name='seller-list'),
    path("buyer/",BuyerListView.as_view(),name='buyer-list'),
    path("<int:pk>/",UserRetrieveView.as_view(),name='user-retrieve'),
    path("<int:pk>/update/",UserUpdateView.as_view(),name='user-update'),
    path("<int:pk>/delete/",UserDeleteView.as_view(),name='user-delete'),
   

   path("login/",UserLoginView.as_view(),name="login"),
   path("logout/",LogoutView.as_view(),name="logout"),

]
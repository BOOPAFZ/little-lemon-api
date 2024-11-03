from django.urls import path
from .views import Category, MenuItemList, SingleMenuItem, ManagerUserView, SingleManagerUserView, OrderView, SingleOrderView, CartView





urlpatterns = [
    path('categories/<int:pk>/', Category.as_view(), name='category-detail'),
    path('items/', MenuItemList.as_view(), name='menuitem-list'),
    path('items/<int:pk>/', SingleMenuItem.as_view(), name='menuitem-detail'),
    path('users/', ManagerUserView.as_view(), name='users'),
    path('users/<int:pk>/', SingleManagerUserView.as_view(), name='single-manager-user'),


    path('cart/menu-items', CartView.as_view()),

    path('orders', OrderView.as_view()),
    path('orders/<int:pk>', SingleOrderView.as_view()),
]

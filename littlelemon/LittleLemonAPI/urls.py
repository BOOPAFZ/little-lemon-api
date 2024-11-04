from django.urls import path
from .views import Category, MenuItemList, SingleMenuItem, ManagerUserView, SingleManagerUserView, OrderView, SingleOrderView, CartView, DeliveryCrewUserView, SingleDeliveryCrewUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token







urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('categories/<int:pk>/', Category.as_view(), name='category-detail'),
    path('items/', MenuItemList.as_view(), name='menuitem-list'),
    path('items/<int:pk>/', SingleMenuItem.as_view(), name='menuitem-detail'),
    path('groups/manager/users', ManagerUserView.as_view()),
    path('groups/manager/users/<int:pk>', SingleManagerUserView.as_view()),
    path('groups/delivery-crew/users', DeliveryCrewUserView.as_view()),
    path('groups/delivery-crew/users/<int:pk>', SingleDeliveryCrewUserView.as_view()),

 


    path('cart/menu-items', CartView.as_view()),

    path('orders', OrderView.as_view()),
    path('orders/<int:pk>', SingleOrderView.as_view()),
]

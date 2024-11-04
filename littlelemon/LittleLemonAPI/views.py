from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Cart, OrderItem, Order
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from rest_framework import generics, viewsets, status
from .serializers import MenuItemSerializer, CategorySerializer, UserSerializer, CartSerializer, OrderSerializer
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle



class CustomViewMixin:
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    throttle_classes = [AnonRateThrottle, UserRateThrottle]



class Category(CustomViewMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemList(CustomViewMixin, generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    http_method_names = ['get', 'post']

class SingleMenuItem(CustomViewMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class ManagerUserView(CustomViewMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        manager_group = Group.objects.get(name='manager')
        return User.objects.filter(groups=manager_group)
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if username:
            user = get_object_or_404(User, username=username)
            manager_group = Group.objects.get(name='manager')
            manager_group.user_set.add(user)
            return Response({'Message': 'User has been added.'}, status=status.HTTP_201_CREATED)
        return Response({'Message': 'Error.'}, status=status.HTTP_400_BAD_REQUEST)



class SingleManagerUserView(CustomViewMixin, generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeliveryCrewUserView(CustomViewMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SingleDeliveryCrewUserView(CustomViewMixin, generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartView(CustomViewMixin, generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderView(CustomViewMixin, generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SingleOrderView(CustomViewMixin, generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
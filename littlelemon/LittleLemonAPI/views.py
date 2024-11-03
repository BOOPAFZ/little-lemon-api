from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Cart, OrderItem, Order
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from rest_framework import generics, viewsets, status
from .serializers import MenuItemSerializer, CategorySerializer, UserSerializer, CartSerializer, OrderSerializer
from django.contrib.auth.models import User, Group

class Category(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    http_method_names = ['get', 'post']

class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class ManagerUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleManagerUserView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeliveryCrewUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SingleDeliveryCrewUserView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SingleOrderView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
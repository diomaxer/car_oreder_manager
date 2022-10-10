from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .models import Colour, Brand, Model, Order
from .serializers import ColourSerializer, BrandSerializer, ModelSerializer, OrderSerializer


# Colour
class ColourView(generics.ListCreateAPIView):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializer


class ColourViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializer


# Brand
class BrandView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# Model
class ModelView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    # def create(self, request, *args, **kwargs):


class ModelViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


# Order
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


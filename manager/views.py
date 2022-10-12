from django.db.models import Count, Sum, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, filters

from .models import Colour, Brand, Model, Order
from .serializers import ColourSerializer, BrandSerializer, ModelSerializer, OrderSerializer, InfoColourSerializer, \
    InfoBrandSerializer


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


class ModelViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


# Order
class OrderPagination(PageNumberPagination):
    page_size = 10


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['model__brand__brand']
    ordering_fields = ['amount']


class OrderViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Info
class InfoColourView(ListAPIView):
    serializer_class = InfoColourSerializer

    def get_queryset(self):
        return Order.objects.all().annotate(title=F('colour__colour')).values('title').annotate(Count('id'), sum=Sum('amount'))


class InfoBrandView(ListAPIView):
    serializer_class = InfoBrandSerializer

    def get_queryset(self):
        return Order.objects.all().annotate(title=F('model__brand__brand')).values('title').annotate(Count('id'), sum=Sum('amount'))

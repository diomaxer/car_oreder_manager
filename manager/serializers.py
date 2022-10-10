import datetime

from rest_framework import serializers

from .models import Colour, Brand, Model, Order


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        if not validated_data['time']:
            validated_data['time'] = datetime.datetime.now()
        return Order.objects.create(**validated_data)

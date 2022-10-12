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

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['brand'] = BrandSerializer(instance.brand).data
        return response


class OrderSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['colour'] = ColourSerializer(instance.colour).data
        response['model'] = ModelSerializer(instance.model).data
        return response


class InfoColourSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    sum = serializers.IntegerField()


class InfoBrandSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    sum = serializers.IntegerField()

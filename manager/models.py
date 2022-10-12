from django.db import models
from django.utils import timezone


class Colour(models.Model):
    """Цвет"""
    colour = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.colour


class Brand(models.Model):
    """Марка"""
    brand = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.brand


class Model(models.Model):
    """Модель"""
    model = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model}, {self.brand.brand}'


class Order(models.Model):
    """Заказ"""
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    amount = models.IntegerField()
    time = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return f'order {self.id}'


"""
from manager.models import *
Colour.objects.create(colour='red')
Brand.objects.create(brand='opel')
Model.objects.create(model='model 1', brand=Brand.objects.get(id=1))
Order.objects.create(colour=Colour.objects.get(id=1), amount=10, model=Model.objects.get(id=1))
"""
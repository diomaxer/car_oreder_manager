from django.urls import path

from .views import *


urlpatterns = [
    path('colour', InfoColourView.as_view()),
    path('brand', InfoBrandView.as_view()),
]
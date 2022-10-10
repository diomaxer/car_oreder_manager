from django.urls import path

from .views import *


urlpatterns = [
    path('', ColourView.as_view()),
    path('<int:pk>', ColourViewDetail.as_view()),
]
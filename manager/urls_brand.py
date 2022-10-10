from django.urls import path

from .views import *


urlpatterns = [
    path('', BrandView.as_view()),
    path('<int:pk>', BrandViewDetail.as_view()),
]

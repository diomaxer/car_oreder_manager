from django.urls import path

from .views import *


urlpatterns = [
    path('', ModelView.as_view()),
    path('<int:pk>', ModelViewDetail.as_view()),
]
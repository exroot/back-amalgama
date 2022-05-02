from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrencyListAPIView.as_view(), name="currencies"),
    path('currencies/<int:id>', views.CurrencyDetailAPIView.as_view(),
         name="currencies")
]
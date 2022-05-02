from django.urls import path
from . import views

urlpatterns = [
    path('registries/', views.RegistryListAPIView.as_view(), name="registries"),
    path('registries/<int:id>', views.RegistryDetailAPIView.as_view(),
         name="registries")
]
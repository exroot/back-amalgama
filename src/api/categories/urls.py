from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name="categories"),
    path('categories/<int:id>', views.CategoryDetailAPIView.as_view(),
         name="categories")
]
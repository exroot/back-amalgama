from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListAPIView.as_view(), name="users"),
    path('users/<int:id>', views.UserDetailAPIView.as_view(),
         name="users")
]
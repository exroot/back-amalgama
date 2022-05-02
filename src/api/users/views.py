import email
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly
from .renderers import UserJSONRenderer
from .serializers import UserSerializer
from .models import User

# Create your views here.
class UserListAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (permissions.IsAuthenticated,IsAdminOrReadOnly) 

    def perform_create(self, serializer):
        return serializer.save(email=self.request.data['email'], is_admin=self.request.data['is_admin'], is_active=self.request.data['is_active'], date_of_birth=self.request.data['date_of_birth'], profile_image=self.request.data['profile_image'], name=self.request.data['name'])
    
    def get_queryset(self):
        return self.queryset.all()

class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (permissions.IsAuthenticated,IsAdminOrReadOnly)
    lookup_field = "id"
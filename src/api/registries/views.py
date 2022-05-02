from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from src.api.categories.models import Category
from src.api.currencies.models import Currency
from src.api.users.models import User
from .permissions import IsOwnerOrReadOnly
from .renderers import RegistryJSONRenderer
from .serializers import RegistrySerializer
from .models import Registry

# Create your views here.
class RegistryListAPIView(ListCreateAPIView):
    serializer_class = RegistrySerializer
    queryset = Registry.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (RegistryJSONRenderer,)
    def perform_create(self, serializer):
        category_object = Category.objects.get(id=self.request.data['category'])
        currency_object = Currency.objects.get(id=self.request.data['currency'])
        return serializer.save(user=self.request.user, title=self.request.data['title'], description=self.request.data['description'], currency=currency_object, type=self.request.data['type'], amount=self.request.data['amount'], category=category_object)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class RegistryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegistrySerializer
    queryset = Registry.objects.all()
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    renderer_classes = (RegistryJSONRenderer,)
    lookup_field = "id"
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from.renderers import CategoryJSONRenderer
from.serializers import CategorySerializer
from.models import Category

# Create your views here.
class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (CategoryJSONRenderer,) 

    def perform_create(self, serializer):
        return serializer.save(category=self.request.data['category'])
    
    def get_queryset(self):
        return self.queryset.all()

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (CategoryJSONRenderer,)
    lookup_field = "id"
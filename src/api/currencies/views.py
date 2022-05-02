from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from .renderers import CurrencyJSONRenderer
from .serializers import CurrencySerializer
from .models import Currency

# Create your views here.
class CurrencyListAPIView(ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    renderer_classes = (CurrencyJSONRenderer,)
    permission_classes = (permissions.IsAuthenticated,) 

    def perform_create(self, serializer):
        return serializer.save(description=self.request.data['description'], symbol=self.request.data['symbol'])
    
    def get_queryset(self):
        return self.queryset.all()

class CurrencyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    renderer_classes = (CurrencyJSONRenderer,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
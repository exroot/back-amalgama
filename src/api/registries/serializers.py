from unicodedata import category
from rest_framework import serializers
from decimal import Decimal

from src.api.categories.serializers import CategorySerializer
from src.api.currencies.serializers import CurrencySerializer
from .models import Registry

class RegistrySerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(
        max_digits=11, 
        decimal_places=2,
        required=True
    )
    user = serializers.CharField(
        required=False
    )
    category = CategorySerializer(required=False, read_only=True)
    currency = CurrencySerializer(required=False, read_only=True)
    class Meta:
        model = Registry
        fields = '__all__'
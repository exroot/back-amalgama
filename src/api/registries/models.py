from django.db import models
from src.api.categories.models import Category
from src.api.currencies.models import Currency
from src.api.users.models import User

class Registry(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    amount = models.DecimalField(default=0.00, max_digits=11, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "registries"
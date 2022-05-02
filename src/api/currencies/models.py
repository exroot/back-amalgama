from django.db import models

# Create your models here.
class Currency(models.Model):
    description = models.CharField(max_length=25)
    symbol = models.CharField(max_length=5, unique=True)
    class Meta:
        db_table = "currencies"
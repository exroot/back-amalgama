from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=25, unique=True)
    class Meta:
        db_table = "categories"
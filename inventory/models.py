from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.IntegerField(default=0)
    min_quantity = models.IntegerField(default=10)
    max_quantity = models.IntegerField(default=100)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

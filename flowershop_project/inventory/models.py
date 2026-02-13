from django.db import models
from django.contrib.auth.models import User

class Flower(models.Model):
    CATEGORY_CHOICES = [
        ('roses', 'Roses'),
        ('tulips', 'Tulips'),
        ('lilies', 'Lilies'),
        ('orchids', 'Orchids'),
        ('seasonal', 'Seasonal'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def needs_reorder(self):
        return self.quantity_in_stock <= self.reorder_level

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return self.name
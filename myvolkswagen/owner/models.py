from django.db import models

# Create your models here.
class Products(models.Model):
    AVAILABILITY_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock')
    ]
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    availablity = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='In Stock')

    def __str__(self):
        return self.name
    
class ProductsImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product.name
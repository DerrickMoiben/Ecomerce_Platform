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
    image = models.ImageField(upload_to='products')
    availablity = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='In Stock')
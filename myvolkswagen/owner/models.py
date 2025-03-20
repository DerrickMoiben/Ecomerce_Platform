from django.db import models

class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock')
    ]
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='In Stock')
    
    # Image fields (up to 6)
    image1 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='products/images/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    name  = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='owner/files/covers')
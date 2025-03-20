from django.db import models


from django.db import models
from datetime import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timenow = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timenow, old_filename)
    return os.path.join('uploads/', filename)

class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock')
    ]
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default='In Stock')
    
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=filepath, blank=True, null=True)



from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timenow = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timenow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    naem = models.TextField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
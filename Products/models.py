from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='media/products/%Y/%M/%D/%y')
    descriptions = models.TextField()
    price = models.PositiveBigIntegerField()
    product_category = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
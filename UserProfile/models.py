from django.db import models

from django.contrib.auth import get_user_model
from Products.models import Products
# Create your models here.

class WishList(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    # for farmers and ranchers
    detail_of_products = models.TextField()
    certifications = models.FileField(upload_to="medai/user_profile/certification/%Y/%M/%D/%y",)
    
import re
from unicodedata import category
from django.db import models


class CategoryProduct(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to = '')
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='category', blank=True, null=True)

    def __str__(self):
        return self.title

class ProductComment(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productcomment')
    text = models.TextField()


    def __str__(self):
        return self.text





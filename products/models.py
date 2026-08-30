from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    thumbnail=models.ImageField(upload_to='product-pics/')
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()

    def __str__(self):
        return self.name
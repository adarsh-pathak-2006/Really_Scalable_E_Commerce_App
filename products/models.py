from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail=models.ImageField(upload_to='product-pics/')
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    is_available=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.stock > 0:
            self.is_available=True
        else:
            self.is_available=False
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class CategoryModel(models.Model):
    uz = models.CharField(max_length=150)
    ru = models.CharField(max_length=150)
    en = models.CharField(max_length=150)
    img = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.uz

class RegionChoises(models.TextChoices):
    TASHKENT = ("TASHKENT", "TASHKENT")
    SAMARKAND = ("SAMARKAND", "SAMARKAND")

class ProductModel(models.Model):
    title_uz = models.CharField(max_length=155)
    title_ru = models.CharField(max_length=155)
    title_en = models.CharField(max_length=155)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="products/")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return f"{self.title_uz} | {self.category}"

class BranchesModel(models.Model):
    name_uz = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    address_uz = models.CharField(max_length=255, null=True, blank=True)
    address_ru = models.CharField(max_length=255, null=True, blank=True)
    address_en = models.CharField(max_length=255, null=True, blank=True)
    time1 = models.CharField(max_length=200)
    time2 = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    region = models.CharField(max_length=100, choices=RegionChoises.choices, default=RegionChoises.TASHKENT)

    def __str__(self):
        return f"{self.name_uz} | {self.address_uz}"
    
class CartModel(models.Model):
    product_id = models.BigIntegerField()
    count = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    
class LikeModel(models.Model):
    product_id = models.BigIntegerField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="like")
    
class OrderModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.BigIntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    branch = models.ForeignKey(BranchesModel, on_delete=models.SET_NULL, related_name="orders", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateField(auto_now_add=True)
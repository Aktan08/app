from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from main.settings import MEDIA_URL


class Company(models.Model):
    name = models.CharField(max_length=255, null=True)
    url = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.name

class SubSubCategory(models.Model):
    name = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.name



class ProductSite(models.Model):
    name = models.CharField(max_length=255, null=True)
    content = models.TextField(max_length=255, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="sites",
        related_query_name="site",
    )
    
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="sites",
        related_query_name="site",
    )
    subsubcategory = models.ForeignKey(
        SubSubCategory,
        on_delete=models.CASCADE,
        related_name="sites",
        related_query_name="site",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="sites",
        related_query_name="site",
    )
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    url = models.TextField(max_length=255, null=True)
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to=MEDIA_URL)
    product = models.ForeignKey(
        ProductSite, on_delete=models.CASCADE, related_name="images"
    )

    def url(image):
        return image.url


class ProductSize(models.Model):
    name = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(
        ProductSite, on_delete=models.CASCADE, related_name="sizes"
    )


class Comment(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(max_length=255, null=True)
    product = models.ForeignKey(
        ProductSite,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
    )
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title

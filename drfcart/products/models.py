from django.db import models


# Create your models here.

class ProductsInfoModel(models.Model):
    productName = models.CharField(max_length=100)
    price = models.FloatField()
    productVendor = models.CharField(max_length=100)
    addeddate = models.DateField()
    def __str__(self):
        return self.productName


class ProductReviewsModels(models.Model):
    userid = models.CharField(max_length=100)
    productName = models.ForeignKey(ProductsInfoModel, on_delete=models.CASCADE, related_name='product_info_reviews')
    reviews = models.CharField(max_length=400)
    rating = models.IntegerField()
    reviewsDate = models.DateField()
    def __str__(self):
        return self.productName


class ProductAvailableModel(models.Model):
    ecommercesite = models.CharField(max_length=100)
    sellername = models.CharField(max_length=100)
    productName = models.ForeignKey(ProductsInfoModel, on_delete=models.CASCADE, related_name='product_info_sale')
    sellingstartfrom = models.DateField()
    def __str__(self):
        return self.productName
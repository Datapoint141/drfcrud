from django.contrib import admin
from products.models import ProductsInfoModel, ProductReviewsModels,ProductAvailableModel
# Register your models here.
class AdminProductInfo(admin.ModelAdmin):
    list_display = ["productName","price","productVendor","addeddate"]
class AdminProductReviews(admin.ModelAdmin):
    list_display = ["userid","productName","reviews","rating","reviewsDate"]
class AdminAvailableSites(admin.ModelAdmin):
    list_display = ["ecommercesite", "sellername", "productName", "sellingstartfrom"]

admin.site.register(ProductsInfoModel,AdminProductInfo)
admin.site.register(ProductReviewsModels,AdminProductReviews)
admin.site.register(ProductAvailableModel,AdminAvailableSites)
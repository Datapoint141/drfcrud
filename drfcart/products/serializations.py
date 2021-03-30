from rest_framework import serializers
from products.models import ProductsInfoModel, ProductReviewsModels,ProductAvailableModel

class ProductReviewsSerailzer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductReviewsModels
class ProductAvailabilitySerailzer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductAvailableModel


class ProductInfoSerailzer(serializers.ModelSerializer):
    product_info_reviews = ProductReviewsSerailzer(read_only=True, many=True)
    product_info_sale = ProductAvailabilitySerailzer(read_only=True, many=True)
    class Meta:
        fields = '__all__'
        model = ProductsInfoModel

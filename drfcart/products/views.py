from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from products.models import ProductsInfoModel, ProductReviewsModels,ProductAvailableModel
from products.serializations import ProductInfoSerailzer,ProductReviewsSerailzer,ProductAvailabilitySerailzer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination,CursorPagination
from rest_framework.filters import BaseFilterBackend
# Create your views here.

class ProductInfoCBV(ListCreateAPIView):
    queryset = ProductsInfoModel.objects.all()
    serializer_class = ProductInfoSerailzer
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]



class ProductCRUDInfoCBV(RetrieveUpdateDestroyAPIView):
    queryset = ProductsInfoModel.objects.all()
    serializer_class = ProductInfoSerailzer
    lookup_field = 'id'
    #authentication_classes = [JSONWebTokenAuthentication, ]
    #permission_classes = [IsAuthenticated, ]


class ProductReviewsCBV(ListCreateAPIView):
    queryset = ProductReviewsModels.objects.all()
    serializer_class = ProductReviewsSerailzer

class ProductReviewsCRUDInfoCBV(RetrieveUpdateDestroyAPIView):
    queryset = ProductReviewsModels.objects.all()
    serializer_class = ProductReviewsSerailzer
    lookup_field = 'id'


class ProductSellingCBV(ListCreateAPIView):
    queryset = ProductAvailableModel.objects.all()
    serializer_class = ProductAvailabilitySerailzer

class ProductSellingCRUDInfoCBV(RetrieveUpdateDestroyAPIView):
    queryset = ProductAvailableModel.objects.all()
    serializer_class = ProductAvailabilitySerailzer
    lookup_field = 'id'


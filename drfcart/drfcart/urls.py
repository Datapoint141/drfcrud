"""drfcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from products import views
#from clientapp import views as client
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="Product Catalog Swagger Views")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('clientapp.urls')),
    path("products/", views.ProductInfoCBV().as_view()),
    path("products/<int:id>/", views.ProductCRUDInfoCBV().as_view()),
    path("reviews/", views.ProductReviewsCBV().as_view()),
    path("reviews/<int:id>/", views.ProductReviewsCRUDInfoCBV().as_view()),
    path("salesat/", views.ProductSellingCBV().as_view()),
    path("salesat/<int:id>/", views.ProductSellingCRUDInfoCBV().as_view()),
    path("get-token/", ObtainJSONWebToken().as_view()),
    path("sg/",schema_view),

]

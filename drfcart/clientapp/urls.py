from django.urls import path
from clientapp import views as client
urlpatterns = [
    path("",client.index),
    path("GetAuthenticationToken/", client.GetAuthenticationToken, name="GetAuthenticationToken"),
    path("GetProductsCatalog/", client.GetProductsCatalog, name="GetProductsCatalog"),
    path("logout/",client.logout, name="logout"),
    path("addProductsForm/", client.addProductsForm, name="addProductsForm"),
    path("AddProductsAction/", client.AddProductsAction, name="AddProductsAction"),
    path("usersProductReviewsForm/",client.usersProductReviewsForm,name='usersProductReviewsForm'),
    path("AddReviewsByProduct/",client.AddReviewsByProduct, name="AddReviewsByProduct"),
    path("AddingProductReviews/",client.AddingProductReviews, name="AddingProductReviews"),

]

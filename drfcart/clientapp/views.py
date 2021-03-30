from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
import json
import requests
BASE_URL = "http://localhost:8000/"

def logout(request):
    #request.session.session_key
    try:
        del request.session['token']
    except:
        return render(request,"index.html")
    #for key in request.session.keys():
        #del request.session[key]
    return render(request,"index.html",{})
def index(request):
    form = UserCreationForm()
    return render(request,"index.html",{'form':form})
def GetAuthenticationToken(request):
    username = request.POST.get('username')
    password = request.POST.get("password")
    dict_data = {
        'username':username,
        'password':password
    }
    ENDPOINT = "get-token/"
    data = json.dumps(dict_data)
    print('user id and password ',dict_data)
    response = requests.post(BASE_URL+ENDPOINT, json=dict_data)
    resp = response.json()
    token = resp['token']
    print("token =", token)
    request.session['token'] = token
    return render(request,"ProductsHome.html",{'token':token})

def GetProductsCatalog(request):
    ENDPOINT = "products/"
    try:
        token = request.session['token']

    except:
        return render(request, "Porducts.html", {"msg": "You dont have token"})
    resp = requests.get(BASE_URL+ENDPOINT, headers={'Authorization': 'jwt ' + token})
    code = resp.status_code

    if code == 401:
        msg = "Signature has expired"
        return render(request, "Porducts.html", {"msg": "Signuture has Expire"})
    else:
        resp = resp.json()
        #print(resp)
    return render(request,"Porducts.html",{"resp":resp})

def addProductsForm(request):
    return render(request,"addproductforms.html",{})

def AddProductsAction(request):
    try:
        token = request.session['token']
    except:
        return render(request, "addproductforms.html", {"msg": "You dont have token"})
    productName = request.POST.get('productName')
    price = request.POST.get('price')
    productVendor = request.POST.get('productVendor')
    addeddate = request.POST.get('addeddate')
    p_dict = {
        'productName':productName,
        'price': price,
        'productVendor': productVendor,
        'addeddate': addeddate,
    }
    p_data = json.dumps(p_dict)
    ENDPOINT = "products/"
    response = requests.post(BASE_URL+ENDPOINT,headers = {'Authorization': 'jwt '+token},json=p_dict)
    resp = response.json()
    print("Response:",resp)
    return render(request, "addproductforms.html", {})

def usersProductReviewsForm(request):

    return HttpResponse('Working Fine')

def AddReviewsByProduct(request):
    productName = request.GET.get('pid')
    p_pk = request.GET.get('pk')
    return render(request,"WriteReviewForm.html",{"productname":productName,'p_pk':p_pk})

def AddingProductReviews(request):
    productName = request.POST.get('productName')
    p_pk = request.POST.get('p_pk')
    username = request.POST.get('username')
    reviews = request.POST.get('reviews')
    reviewdate = request.POST.get('reviewdate')
    rating = request.POST.get('rating')
    data = {
        "productName":p_pk,
        "userid":username,
        "reviews":reviews,
        "reviewsDate":reviewdate,
        "rating":rating
    }
    ENDPOINT ="reviews/"
    p_dict = json.dumps(data)
    url = BASE_URL + ENDPOINT
    response = requests.post(url,  json=data)
    return render(request,"Porducts.html",{"resp":response})
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.hello),
    path('/greet',views.greet),
    path('/extra',views.extra),
    path('/demolist',views.demolist),
    path('/loadlogin',views.loadlogin),
    path('/login',views.login,name="login"),
    path('/register',views.register),
    path('/signup',views.loadsignup,name="signup"),
    path('/home',views.home),
    path('/uploadproduct',views.loaduploadproduct,name="uploadProject"),
    path('/uploadprod',views.uploadprod),
    path('/portfolio',views.protfolio),
    path('/portfolio2',views.portfolio2),
    path('/allproducts',views.allproducts,name="allProducts"),
    path('/productdetails/',views.productdetails,name="proInfo"),
    path('/addProductImage/',views.addProductImage,name="upProImage"),
    path('/addProductVideo/',views.addProductVideo,name="upProVideo"),
    #path('/productInfo/',views.ProductInfo),
    path('/addProductBid/',views.addProductBid,name="addBid"),
    path('/addProductQuestions/',views.addProductQuestions,name="addQues"),
    path('/myProducts/',views.myProducts,name="mypro"),
    path("/deleteBid/",views.deleteBid,name="delBid"),
    path("/myBids",views.myBids,name="myBids"),
    path("/sellBids/",views.sellBids,name="sellBids"),
    path("/logout",views.logout,name="logout"),
    path("/addSave/",views.addToSave,name="addSave"),
    path("/removeSave/",views.removeFromSave,name="removeSave"),
    path("/loadSaves",views.loadsaves,name="loadSaves"),
    path("/home",views.home,name="Home")
]

admin.site.site_header="Exotic Streetwear"
admin.site.site_title="Exotic Streetwear"
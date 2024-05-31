from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from itertools import chain

def hello(request):
    return HttpResponse("Harsh Choski")

def greet(request):
    return HttpResponse("Good morning")

def extra(request):
    return render(request,"newTemp.html")

def demolist(request):
    myList=[
            {"sname":"Harsh","rno":"09"},
            {"sname":"Amman","rno":"10"},
            {"sname":"Mayur","rno":"11"}   
           ]
    return render(request,"demolist.html",{"myList":myList})

def loadlogin(request):
    return render(request,"login.html")

def login(request):
    uname=request.POST.get("txtuname")
    pwd=request.POST.get("txtpwd")

    luser=user.objects.filter(username=uname,password=pwd).first()
    if(luser):
        request.session["uid"]=luser.userid
        request.session["uname"]=luser.username
        
        return redirect('./home')
    else:
        temp={"msg":"Invalid username or password"}
        return render(request,"login.html",temp)

def logout(request):
    del request.session["uid"]
    del request.session["uname"]

    return redirect("login")

def loadsignup(request):
    return render(request,"signup.html")

def register(request):
    uname=request.POST.get("txtuname")
    pwd=request.POST.get("txtpwd")
    mail=request.POST.get("txtemail")
    gender=request.POST.get("gen")
    dob=request.POST.get("dob")
    contactno=request.POST.get("contactno")
    #city=request.POST.get("")
    biodata=request.POST.get("bio")
    image=request.FILES.get("fup")
    ct=city.objects.filter(cityid=request.POST.get("txtcity")).first()

    print(ct)
    us=user(username=uname,password=pwd,email=mail,gender=gender,dob=dob,contactno=contactno,cityid=ct,bio=biodata,profileImage=image)
    us.save()
    
    return redirect('./loadlogin')

def home(request):
    if "uid" not in request.session:
        return redirect ("./login")
    
    return render(request,"home.html")

def loaduploadproduct(request):
    if "uid" not in request.session:
        return redirect ("./login")
     
    return render(request,"uploadproduct.html")

def uploadprod(request):
    if "uid" not in request.session:
        return redirect ("./login")
    
    userinfo=user.objects.filter(userid=request.session["uid"]).first()
    upprod=product(userid=userinfo,prodtitle=request.POST.get("txtptitle"),brand=request.POST.get("txtbrand"),desc=request.POST.get("txtdesc"),mandate=request.POST.get("txtmandate"),adddate=request.POST.get("txtaddeddate"),auctdate=request.POST.get("txtauctdate"),auctienddate=request.POST.get("txtauctendndate"),pimg=request.FILES.get("fup"),price=request.POST.get("txtprice"))
    upprod.save()    
    return redirect("./myProducts")

def protfolio(request):
    if "uid" not in request.session:
        return redirect ("./login")
    

    useri=user.objects.filter(userid=request.session["uid"]).first()
    temp={
        "userInfo":useri,
        "products":product.objects.filter(userid=request.session["uid"]).values()
    }

    print(temp["products"])
    return render(request,"portfolio.html",temp)

def portfolio2(request):
    if "uid" not in request.session:
        return redirect ("./login")
    

    useri=user.objects.filter(userid=request.session["uid"]).first()
    temp={
        "userInfo":useri,
        "products":product.objects.filter(userid=request.session["uid"]).values()
    }

    return render(request,"portfolio2.html",temp)

def loadproductdetails(request):
    if "uid" not in request.session:
        return redirect ("./login")
    
    return render('./productdetails')

def productdetails(request):
    if "uid" not in request.session:
        return redirect ("./login")
    
    id=request.GET.get('id')
    p=product.objects.filter(productid=id).first()
    img=pimages.objects.filter(productid=id)
    vid=pvideos.objects.filter(productid=id)
    pbid=productbid.objects.filter(productid=id)
    question=questions.objects.filter(productid=p)
    u=user.objects.filter(userid=request.session["uid"]).first()
    myBids=productbid.objects.filter(productid=id).filter(userid=u)

    mySaves=save.objects.filter(
        userid=u,
        productid=p
    )
    temp={
        "products":product.objects.all(),
        "productInfo":p,
        "pimages":img,
        "pvideos":vid,
        "productbid":pbid,
        "questions":question,
        "bid":productbid.objects.filter(productid=p),
        "totalBids":len(pbid),
        "myBids":len(myBids),
        "mySaves":len(mySaves)
    }
    return render(request,"productdetails.html",temp)

def deleteBid(request):
    if "uid" not in request.session:
        return redirect ("./login")
    

    id=request.GET.get('id')
    bid=request.GET.get('bid')
    productbid.objects.filter(prodbidid=bid).delete()
    return redirect("../productdetails/?id="+id)

def allproducts(request):
    if "uid" not in request.session:
        return redirect ("./login")
    

    if(request.POST.get('btnSearch')):
        if(request.POST.get('cat')):
            cid=request.POST.get('cat')
            products=product.objects.filter(category=category.objects.filter(categoryid=cid).first())
            
        if(request.POST.get('minprice') ):
            mp=request.POST.get('minprice')
            products=products.filter(min_bid>=mp)

        if(request.POST.get('maxprice')):
            mp=request.POST.get('maxprice')
            products=products.filter(min_bid>=mp)
        
    else:
        products=product.objects.all()
    temp={
        "productInfo":id,
        "products":products,
        "cat":category.objects.filter().all()
    }
    return render(request,"allproducts.html",temp)

def myProducts(request):
    if "uid" not in request.session:
        return redirect ("../login")
    
    userinfo=user.objects.filter(userid=request.session["uid"]).first()
    
    p=product.objects.filter(userid=userinfo).values()
    
    for x in p:
        xx=productbid.objects.filter(productid=x["productid"]).values()
        print("-------\n\n",x,"------\n\n")
        x["category"]=category.objects.filter(categoryid=x["category_id"]).first()
        x["userid"]=user.objects.filter(userid=x["userid_id"]).first()
        if(len(xx)==0):
            x["bids"]=0
            x["totalBids"]=0
            x["avgBids"]=0
            x["maxBid"]=0
        else:

            x["bids"]=xx
            x["totalBids"]=len(xx)
            tot=0
            mbid=xx[0]["amount"]
            for xxx in xx:
                if mbid<xxx["amount"]:
                    mbid=xxx["amount"]
                tot+=xxx["amount"]/x["totalBids"]

            x["avgBids"]=round(tot,2)   
            x["maxBid"] =mbid 

    temp={
        "products":p
    }
    return render(request,"myProducts.html",temp)

def addProductImage(request):
    
    pid=request.GET.get("pid")

    p=pimages(productid=product.objects.filter(productid=pid).first(),
              imageurl=request.FILES.get("fup"),
              description=request.POST.get("desc"), 
              userid=user.objects.filter(userid=request.session["uid"]).first()
            )
    p.save()
    return redirect("../productdetails/?id="+str(pid))

def addProductVideo(request):
  
    pid=request.GET.get("pid")

    p=pvideos(productid=product.objects.filter(productid=pid).first(),
              videourl=request.FILES.get("fup2"),
              description=request.POST.get("desc"),
              userid=user.objects.filter(userid=request.session["uid"]).first())
    p.save()
    return redirect("../productdetails/?id="+str(pid))

def addProductBid(request):
    pid=request.GET.get("pid")

    p=productbid(productid=product.objects.filter(productid=pid).first(),
                 userid=user.objects.filter(userid=request.session['uid']).first(),
                 amount=request.POST.get("txtbid")             
                 )
    p.save()
    return redirect("../productdetails/?id="+str(pid))

def addProductBid(request):
    

    pid=request.GET.get("pid")

    p=productbid(
        productid=product.objects.filter(productid=pid).first(),
        userid=user.objects.filter(userid=request.session['uid']).first(),
        amount=request.POST.get("txtbid")             
        )
    p.save()
    return redirect("../productdetails/?id="+str(pid))

def addProductQuestions(request):
     

    pid=request.GET.get("pid")

    q=questions(
        productid=product.objects.filter(productid=pid).first(),
        userid=user.objects.filter(userid=request.session['uid']).first(),
        question=request.POST.get("txtques"),
        answer=request.POST.get("txtans")
    )
    q.save()
    return redirect("../productdetails/?id="+str(pid))

def myBids(request):
    ui=user.objects.filter(userid=request.session["uid"]).first()
    mybids=productbid.objects.filter(userid=ui).values()

    bids=[]
    for x in mybids:
        bids.append(x["productid_id"])
    #print("\n==============\n",bids,"\n==================\n")
    
    p=product.objects.filter(productid__in=bids ).values()
    
    for x in p:
        xx=productbid.objects.filter(productid=x["productid"]).values()
        x["category"]=category.objects.filter(categoryid=x["category_id"]).first()
        x["userid"]=user.objects.filter(userid=x["userid_id"]).first()
        x["bids"]=xx
        x["totalBids"]=len(xx)
        tot=0
        mbid=xx[0]["amount"]
        for xxx in xx:
            if mbid<xxx["amount"]:
                mbid=xxx["amount"]
            tot+=xxx["amount"]/x["totalBids"]

        x["avgBids"]=round(tot,2)   
        x["maxBid"] =mbid 

    temp={
        "products":p
    }
    return render(request,"myBids.html",temp)

def sellBids(request):
    
    pid=request.GET.get("pid")
    bid=request.GET.get("bid")

    prod=product.objects.filter(productid=pid).first()
    prod.status=1
    prod.selectedBidId=bid
    prod.save()
    return redirect("../productdetails/?id="+str(pid))

def addToSave(request):
    pid=request.GET.get("pid")
    addSave=save(
        productid=product.objects.filter(productid=pid).first(),
        userid=user.objects.filter(userid=request.session['uid']).first()
    )
    addSave.save()
    return redirect("../productdetails/?id="+str(pid))

def removeFromSave(request):
    pid=request.GET.get("pid")

    removeSave=save.objects.filter(
        productid=product.objects.filter(productid=pid).first(),
        userid=user.objects.filter(userid=request.session['uid']).first()
    )
    removeSave.delete()

    return redirect("../productdetails/?id="+str(pid))

def loadsaves(request):
    if "uid" not in request.session:
        return redirect ("../login")
    

    userinfo=user.objects.filter(userid=request.session["uid"]).first()
    
    saves=save.objects.filter(userid=userinfo)
    plist=[]
    for x in saves:
        plist.append(x.productid.productid)

    p=product.objects.filter(productid__in=plist).values()
    
    for x in p:
        xx=productbid.objects.filter(productid=x["productid"]).values()
        print("-------\n\n",x,"------\n\n")
        x["category"]=category.objects.filter(categoryid=x["category_id"]).first()
        x["userid"]=user.objects.filter(userid=x["userid_id"]).first()
        if(len(xx)==0):
            x["bids"]=0
            x["totalBids"]=0
            x["avgBids"]=0
            x["maxBid"]=0
        else:

            x["bids"]=xx
            x["totalBids"]=len(xx)
            tot=0
            mbid=xx[0]["amount"]
            for xxx in xx:
                if mbid<xxx["amount"]:
                    mbid=xxx["amount"]
                tot+=xxx["amount"]/x["totalBids"]

            x["avgBids"]=round(tot,2)   
            x["maxBid"] =mbid 

    temp={
        "products":p
    }
    return render(request,"myProducts.html",temp)

# def ProductInfo(request):
#     id=request.GET.get("id")
#     pid=request.GET.get("pid")
#     bids=productbid.objects.filter(productid=pid)
#     question=questions.objects.filter(questionid=pid)

#     productInfo=pimages.objects.filter(productImageId=pid)
#     temp={
#         "productImage":productInfo,
#         "productbid":bids,
#         "questions":question
#     }
#     return redirect("../productdetails/?id="+str(pid),temp)
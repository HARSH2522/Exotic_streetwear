from django.db import models

class country(models.Model):
    countryid=models.AutoField(primary_key=True)
    countryname=models.TextField(max_length=20)

    def __str__(self):
        return self.countryname
    
class state(models.Model):
    stateid=models.AutoField(primary_key=True)
    statename=models.TextField(max_length=20)
    countryid=models.ForeignKey(country,on_delete=models.CASCADE)

    def __str__(self):
        return self.statename
    
class city(models.Model):
    cityid=models.AutoField(primary_key=True)
    cityname=models.TextField(max_length=20)
    stateid=models.ForeignKey(state,on_delete=models.CASCADE)

    def __str__(self):
        return self.cityname
      
class user(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.TextField(max_length=20)
    password=models.TextField(max_length=20)
    email=models.EmailField(max_length=50,default="")
    gender=models.TextField(max_length=10,null=True)
    dob=models.DateField(null=True)
    contactno=models.TextField(max_length=20,default="")
    cityid=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    regDateTime=models.DateTimeField(auto_now=True)
    bio=models.TextField(max_length=1000,null=True)
    profileImage=models.ImageField(upload_to='media/images',default="default.jpg")
    
    def __str__(self):
        return str(self.userid)
    
class category(models.Model):
    categoryid=models.AutoField(primary_key=True)
    categoryname=models.TextField(max_length=50)
    status=models.IntegerField(default=1)

    def __str__(self):
        return self.categoryname

class product(models.Model):
    productid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    prodtitle=models.TextField(max_length=100)
    brand=models.TextField(max_length=30)
    desc=models.TextField(max_length=200)
    mandate=models.DateField(null=True)
    min_bid=models.IntegerField(default="1")
    adddate=models.DateTimeField(auto_now=True)
    auctdate=models.DateField(null=True)
    auctienddate=models.DateField(null=True)
    pimg=models.ImageField(upload_to="media/images",default="default.jpg")
    price=models.TextField(max_length=50,default=1)
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=0)
    selectedBidId=models.IntegerField(null=True,default=-1)
    def __str__(self):
        return str(self.productid)
        
class productbid(models.Model):
    prodbidid=models.AutoField(primary_key=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(default=0)
    bidDateTime=models.DateTimeField(auto_now=True)
    status=models.IntegerField(default=1)

    def __str__(self):
        return str(self.prodbidid)  
    
class questions(models.Model):
    questionid=models.AutoField(primary_key=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    question=models.TextField(max_length=500)
    DateTime=models.DateTimeField(auto_now=True)
    answer=models.TextField(max_length=500)

    def __str__(self):
        return str(self.questionid)      

 
class userTransaction(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    transaction_Date=models.DateField(null=True)
    transaction_Time=models.TimeField(null=True)
    transaction_amount=models.IntegerField(default=0)
    product_id=models.ForeignKey(product,on_delete=models.DO_NOTHING,null=True)

    status=models.IntegerField(default=1)
    fromUserid=models.IntegerField(default=0)
    toUserid=models.IntegerField(default=0)
    def __str__(self):
        return self.transaction_id
    
class save(models.Model):
    saveid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "username-"+self.userid.username+" productTitle-"+self.productid.prodtitle
    
class pimages(models.Model):
    productImageId=models.AutoField(primary_key=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    imageurl=models.ImageField(upload_to="media/images",default="default.jpg")
    description=models.TextField(max_length=200)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.productImageId)
    
class pvideos(models.Model):
    productVideoId=models.AutoField(primary_key=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    #vidoeid=models.TextField(max_length=200)
    videourl=models.ImageField(upload_to="media/video",default="default.jpg")
    description=models.TextField(max_length=200)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.productVideoId)
    

    
class complaint(models.Model):
    complaintid=models.AutoField(primary_key=True)
    #fromuserid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    productid=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    description=models.TextField(max_length=500)
    complaintDateTime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.complaintid

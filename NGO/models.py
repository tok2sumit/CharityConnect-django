from django.db import models
from django.contrib.auth.models import User

class NGO(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='static/profile_pic/NGO/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status= models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
        
class Requirements(models.Model):
    nid = models.IntegerField()
    ename = models.CharField(max_length=100)
    edescription = models.TextField()
    edate = models.DateField()
    ereq = models.IntegerField()

class Contact(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    phoneno=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    querry=models.TextField()
    date=models.DateField()

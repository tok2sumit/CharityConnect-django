from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='static/profile_pic/Donor/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Feed(models.Model):
    Name = models.CharField(max_length= 40)
    email = models.CharField(max_length= 40)
    feed= models.TextField(max_length=500)

class Donation(models.Model):
    donor_id=models.IntegerField()
    amount=models.IntegerField()
    ename=models.CharField(max_length=100)

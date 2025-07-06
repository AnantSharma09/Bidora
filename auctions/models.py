from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Auction_model(models.Model): 
   title = models.CharField(max_length=255)
   description = models.TextField()
   starting_bid = models.IntegerField(default=0)
   sold_at = models.IntegerField(default=0)
   image = models.ImageField(upload_to='auctions/',blank=True,null=True)
   created_at = models.DateTimeField(auto_now_add = True)
   created_by = models.ForeginKey(User,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.title
   
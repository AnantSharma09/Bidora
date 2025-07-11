from django.db import models
from django.contrib.auth.models import User
from datetime import date,time
from django.utils import timezone
# Auction Model (Post / Listing)
class AuctionModel(models.Model):
    # User Info
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    # Optional reference to profile verification status
    is_verified = models.BooleanField(default=False)  # You can sync this in view
    
    # Date and Time for auction 
    
    date_of_auction = models.DateField(default=date(2025,7,10))
    time_of_auction = models.TimeField(default=time(12,0))

    # Product Info
    product_name = models.CharField(max_length=300)
    description = models.TextField()
    unique_points = models.TextField(blank=True, null=True)
    product_age = models.CharField(max_length=100)
    starting_bid = models.PositiveIntegerField()
    image = models.ImageField(upload_to='auction_images/')

    # Verification & Payment
    premium_verification = models.BooleanField(default=False)
    bank_account_linked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    # is live function
    def is_live(self):
        now=timezone.now()
        return self.date_of_auction == now.date() and self.time_of_auction <= now.time() 

    def __str__(self):
        return self.title
    
class RegistrationModel(models.Model):
    auction = models.ForeignKey(AuctionModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Redundant but may be useful if auction host wants viewer info
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
     
    # Optional status fields (these could be fetched from user profile)
    premium_verification = models.BooleanField(default=False)
    bank_account_linked = models.BooleanField(default=False)
    gov_id_linked = models.BooleanField(default=False)

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('auction', 'user')  # Prevent double registrations

    def __str__(self):
        return f"{self.user.username} registered for {self.auction.title}"
    
    
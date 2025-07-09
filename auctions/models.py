from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.title

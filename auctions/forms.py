from django import forms 
from .models import AuctionModel,RegistrationModel

class AuctionForm(forms.ModelForm):
    class Meta:
        model = AuctionModel
        fields = [
            'full_name', 'age', 'country', 'city',
            'product_name', 'description', 'unique_points', 'product_age',
            'starting_bid', 'image', 'premium_verification', 'bank_account_linked',
            'time_of_auction','date_of_auction'
        ]



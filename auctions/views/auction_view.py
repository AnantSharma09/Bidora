from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404
from auctions.forms import AuctionForm,RegristrationForm
from auctions.models import AuctionModel,RegistrationModel 
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 

@login_required
def create_auction_view(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.created_by = request.user
            auction.save()
            return redirect('feed')
    else:
          form = AuctionForm()

    return render(request, 'auction/create_auction.html', {'form': form})

def auction_detail_view(request, auction_id):
    auction = get_object_or_404(AuctionModel, id=auction_id)
    return render(request, 'auction/auction_detail.html',{'auction':auction})

@login_required
def auction_registration_view(request, auction_id):
    auction = get_object_or_404(AuctionModel, id=auction_id)

    if request.method == 'POST':
        form = RegristrationForm(request.POST)
        if form.is_valid():
            # Check if already registered
            already_registered = RegistrationModel.objects.filter(
                auction=auction, user=request.user).exists()
            if already_registered:
                messages.warning(request, "You have already registered for this auction.")
                return redirect('auction_detail', auction_id=auction.id)

            # Extract cleaned data from the form
            age = form.cleaned_data.get('age', 0)
            gov_id = form.cleaned_data.get('gov_id_linked')
            bank = form.cleaned_data.get('bank_account_linked')

            if age < 18 or not (gov_id and bank):
                messages.warning(request, "You must be 18+ and have government ID and bank linked to register.")
                return redirect('auction_detail', auction_id=auction.id)

            # Save the registration
            registration = form.save(commit=False)
            registration.auction = auction
            registration.user = request.user
            registration.save()
            send_mail(
                subject='Auction Regristration Confirmation',
                message=f'Dear {request.user.username},\n\nYou have successfully registered for the auction: "{auction.product_name}".\n\nAuction Date: {auction.date_of_auction}\nTime: {auction.time_of_auction}\n\nThank you for using Bidora!',
                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )
            
            messages.success(request, "You are now registered for the auction,Please check your mail.")
            return redirect('auction_detail', auction_id=auction.id)
    else:
        form = RegristrationForm()

    return render(request, 'auction/auction_detail.html', {
        'form': form,
        'auction': auction
    })


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404
from auctions.forms import AuctionForm
from auctions.models import AuctionModel,RegistrationModel 
from django.contrib import messages

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

@ login_required
def auction_registration_view(request,auction_id):
    auction = get_object_or_404(AuctionModel,id=auction_id)
    
    already_registered = RegistrationModel.objects.filter(auction=auction,user=request.user).exists()
    if already_registered:
        messages.warning(request,"Your have already registered for this auction.")
        return redirect('auction_detail',auction_id=auction.id)
    
    RegistrationModel.objects.create(
        auction = auction,
        user = request.user,
        name = request.user.get_full_name() or request.user.username,
        age=18,
        country="Unknown",
        premium_verification=False,
        bank_account_linked=False,
        gov_id_linked=False,
    )
    messages.success(request,"You have been successfully registered for the auction.")
    return redirect('auction_detail',auction_id=auction.id)
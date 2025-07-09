from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404
from auctions.forms import AuctionForm
from auctions.models import AuctionModel


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
from django.urls import path
from .views import auth_views 
from .views import auction_view

urlpatterns = [
  path('signup/', auth_views.signup, name='signup'),
  path('activation/<str:token>/',auth_views.activation_view, name='activation'),
  path('login/',auth_views.login_view,name='login'),
  path('feed/',auth_views.feed_view,name='feed'),
  path('logout/',auth_views.logout_view,name='logout'),
  path('create_auction/',auction_view.create_auction_view,name='create_auction'),
  path('auction/<int:auction_id>/', auction_view.auction_detail_view, name='auction_detail'),
]
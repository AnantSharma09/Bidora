from django.urls import path
from .views import auth_views 

urlpatterns = [
  path('signup/', auth_views.signup, name='signup'),
  path('activation/<str:token>/',auth_views.activation_view, name='activation'),
  path('login/',auth_views.login_view,name='login'),
  path('feed/',auth_views.feed_view,name='feed'),
]
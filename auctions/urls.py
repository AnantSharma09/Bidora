from django.urls import path
from .import views 

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('activation/<str:token>',views.activation_view, name='activation'),
  path('login/',views.login_view,name='login'),
  path('feed/',views.feed_view,name='feed'),
]
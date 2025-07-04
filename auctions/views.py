from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.signing import Signer
from django.core.signing import BadSignature

signer = Signer()

def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if not (username and email and password):
      return render(request,'signup.html',{'error':'All fields are required.'})
    
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
      return render(request,'signup.html',{'error':'Email or Username already exist.'})
    
    user = User.objects.create_user(username= username, email=email,password=password)
    user.is_active=False
    user.save()

    token = signer.sign(user.pk)
    activation_link = request.build_absolute_uri(f'/activation/{token}/')

    send_mail(
       'Account activation mail',
       f'click the link to activate:{activation_link}',
       'noreply@bidora.com',
       [email],
    )

    return render(request,'signup.html',{'success':'Activation email sent. check your inbox'})
  return render(request,'signup.html')

def activation_view(request,token):
    try:
      user_id = signer.unsign(token)

      user = User.objects.get(pk=user_id)

      if user.is_active:
        return HttpResponse("Account already activated.")
     
      user.is_active = True
      user.save()

      return HttpResponse('Account activated successfully! You can now login.')
   
    except BadSignature:
        return HttpResponse("Invalid or tampered activation link.")
    except User.DoesNotExist:
        return HttpResponse("User not found.")
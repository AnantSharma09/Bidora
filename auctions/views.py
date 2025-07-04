from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (username and email and password):
            return render(request, 'signup.html', {'error': 'All fields are required'})
        
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Username or email already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, 'signup.html', {'success': 'User created successfully'})
    
    return render(request, 'signup.html')
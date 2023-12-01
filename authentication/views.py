from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method =='POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        print(fullname,username,email,password,confirmpassword)
        if not username or not email or not password or not confirmpassword:
            messages.error(request,'Please check again')
            return render(request,'authentication/signup.html',)
        if len(password) < 8:
            messages.error(request,'Password is less than 8 characters')
            return render(request,'authentication/signup.html',)
        if password != confirmpassword:
            messages.error(request,'Password is not the same')
            return render(request,'authentication/signup.html',)
        username_exist = User.objects.filter(username = username).exists()
        if username_exist:
            messages.error(request, 'The username already exist')   
            return render(request,'authentication/signup.html')
        email_exist = User.objects.filter(email = email).exists()
        if email_exist:
            messages.error(request, 'The email already exist')   
            return render(request,'authentication/signup.html')
        user = User.objects.create(username = username,
                                  email = email,
                                  first_name = fullname)
        user.set_password(password)
        user.save()
        messages.success('Account created sucessfully')
        
    return render(request,'authentication/signup.html',)
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
    print("Came here for register")
    if request.method == 'POST':
        print("This is post request")
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['user_name']
        emailId = request.POST['email_id']
        password = request.POST['pass']
        confirmPassword = request.POST['confirmpass']
        if password == confirmPassword:
            if User.objects.filter(username=userName).exists() == False or User.objects.filter(email=emailId).exists() == False:
                user = User.objects.create_user(username=userName, password=password, email=emailId, first_name=firstName, last_name=lastName)
                user.save()
                print("User Added successfully")
                return render(request, 'signin.html')
            else:
                print("User already exists")
                messages.info(request, "User already exists")
                return redirect('register')
        else:
            print("User already exists")
            messages.info(request, "Password not matching")
            return redirect('register')
    else:
        print("This is Get request")
        return render(request, 'register.html')

def sign(request):
    print("Came here for signin")
    if request.method == 'POST':
        print("This is post request")
        userName = request.POST['user_name']
        passwd = request.POST['pass']
        print("username:", userName, " password:", passwd)
        user = auth.authenticate(username=userName, password=passwd)
        if user is not None:
            auth.login(request, user)
            print("sign in successfull")
            return redirect('/swp')
        else:
            messages.info(request, "Invalid credential. Please give valid email and password")
            print("invalid sign in")
            return redirect('sign')
    else:
        print("This is Get request")
        return render(request, 'signin.html')
    
def signout(request):
    print("Came here for signout")
    auth.logout(request)
    print("auth signout done")
    return redirect('/swp')
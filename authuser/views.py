from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# register user
def register(request):
    if request.method == "POST":
        print(request.POST)
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("uname")
        password = request.POST.get("pasw")
        try:
            User.objects.get(username=username)
            # return render(request, "register.html", 
            # {"error": "Username already exists"})
            messages.error(request,'Username already exists..!')
            return redirect('register')
        except :
            a = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                email=email,
                username=username,
                password=password,
            )
    return render(request, "register.html")

# login user
def login_(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pasw")
        user = authenticate(username=username, password=password)
        print(user)  
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password..!')
            return redirect('login_')
    return render(request,'login.html')

# logout user
def logout_(request):
    logout(request)
    messages.success(request,'logout successfull..!!')
    return redirect(login_)

# profile user
@login_required
def profile(request):
    return render(request,'profile.html')

# Reset password
@login_required
def reset_pasw(request):

    if request.method == 'POST':

        # Verify Old Password
        if 'old_pasw' in request.POST:
            old_pasw = request.POST['old_pasw']
            u = authenticate(username=request.user.username,password=old_pasw)
            if u:
                return render(request,'reset_pasw.html',{'new': True})
            messages.error(request,'Entered old password is wrong..!')
            return redirect('reset_pasw')

        # Update Password
        if 'new_pasw' in request.POST:
            new_pasw = request.POST['new_pasw']
            confirm_pasw = request.POST['confirm_pasw']

            # Check password match
            if new_pasw != confirm_pasw:
                messages.error(request,'New Password and Confirm Password do not match!')

                return render(request,'reset_pasw.html',{'new': True})
            user = request.user

            # Check same old password
            if user.check_password(new_pasw):
                messages.error(request,'New password cannot be same as old password!')
                return render(request,'reset_pasw.html',{'new': True})
            user.set_password(new_pasw)
            user.save()

            update_session_auth_hash(request,user)
            messages.success(request,'Password updated successfully!')
            return redirect('profile')

    return render(request,'reset_pasw.html')
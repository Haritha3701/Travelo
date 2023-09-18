from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        u_name = request.POST["uname"]
        pass1 = request.POST["password"]
        user = auth.authenticate(username=u_name, password=pass1)

        if user is not None:
            auth.login(request, user)
            print("Login Successful")
            return redirect('/')
        else:
            messages.info(request, "Invalid username and password")
            return redirect('loginpage')

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        u_name = request.POST["uname"]
        f_name = request.POST["fname"]
        l_name = request.POST["lname"]
        email = request.POST["e_mail"]
        pass1 = request.POST["password"]
        pass2 = request.POST["conf_password"]

        if pass1 == pass2:

            if User.objects.filter(username=u_name).exists():
                messages.info(request, "Username already taken")
                return redirect("registerpage")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect("registerpage")
            else:
                user = User.objects.create_user(username=u_name, first_name=f_name, last_name=l_name, email=email,
                                                password=pass1)

                user.save();
                print("New user registered")
                return redirect('loginpage')

        else:
            messages.info(request, "Password and confirm password are not same")
            return redirect("registerpage")

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request,id):
    return render(request, "students/home.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)
        if not user.exists():
            message.error(req,"username is invalid")
            return redirect('/logic/')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "students/login.html")
def register(request):
    if request.method == "POST":
        # your logic
        pass

    return render(request, "students/register.html")

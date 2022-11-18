from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.

def index(request):
    # default 1st page
    return render(request, "base/index.html",{
    })

def login_view(request):
    if request.method=="POST":
        # form submitted here

        # attempt to sign in
        username= request.POST["username"]
        password=request.POST["password"]
        role = request.POST["role"]
        user= authenticate(request, username= username, password=password, role= role) 

        if user is not None:
            if role==admin:
                return HttpResponseRedirect(reverse("admin"))
            elif role== doctor:
                return HttpResponseRedirect(reverse("doctor"))
            else:
                return HttpResponseRedirect(reverse("patient"))
        else:
            return render(request, "base/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "base/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



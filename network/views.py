from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime

from .models import User, Post


def index(request):
    # Checking if user sent a post by POST method
    if request.method == "POST":
        # Get what was posted by the user
        posted = request.POST["posted"]

        
        # Preparing all fields needed to add an entry to Post Model
        user = request.user
        post = posted
        now = datetime.now()
        likes = 0

        # Saving the new post in Post Model
        newpost = Post(userid=user, post=post, datetime=now, likes=likes)
        newpost.save()


        return render(request, "network/index.html", {
            # Passing all posts from database (with latest first) to display them later
            "posts": Post.objects.all().order_by('-id'),
            "posted": posted,
        })


    else:    
        return render(request, "network/index.html", {
            # Passing all posts from database (with latest first) to display them later
            "posts": Post.objects.all().order_by('-id')
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile_page(request, username):
    
    # Is this user registred in oru database? 
    # TODO

    # If so, dispaly this users, data
    user_profiled = User.objects.filter(username=username)


    return render(request, "network/profile.html", {
                "username": username,
                "user_profiled": user_profiled
            })


from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime

from .models import User, Post, Follower


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

    # TODO try!!!!!!!
    
    # Does the user exist?
    try: 
        user_profiled = User.objects.filter(username=username)

        user_profiled_id = user_profiled.values_list('id', flat=True)
        user_profiled_id = user_profiled_id[0]

        # Get this user's posts
        user_posts = Post.objects.filter(userid=user_profiled_id).order_by('-id')

        # Count the amount of followers for this user
        amount_of_followers = Follower.objects.filter(followed=user_profiled_id).count()

        # Count how many people this user is following
        amount_of_following = Follower.objects.filter(follower=user_profiled_id).count()

        # Checking the name of who is logged in
        user_logged_in = request.user.id

        # Checking if user_logged_in is following user in profile
        isfollowing = Follower.objects.filter(followed=user_profiled_id ,follower=user_logged_in).count()

        return render(request, "network/profile.html", {
                    "username": username,
                    "user_profiled": user_profiled,
                    "user_profiled_id": user_profiled_id,
                    "amount_of_followers": amount_of_followers,
                    "amount_of_following": amount_of_following,
                    "user_logged_in": user_logged_in,
                    "isfollowing": isfollowing,
                    "user_posts": user_posts
                })

    # If not, display page without posts
    except IndexError:
        return render(request, "network/missingprofile.html", {
                    "username": username,
                })


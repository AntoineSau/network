from typing import Iterable
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt


# test Paginator
from django.core.paginator import Paginator

from .models import User, Post, Follower, Like



def index(request):
    user = request.user
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


        # PAGINATOR
        posts = Post.objects.all().order_by('-id')
        paginator = Paginator(posts, 10) # test Paginator with 10 per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        return render(request, "network/index.html", {
            # Passing all posts from database (with latest first) to display them later
            "posts": posts,
            "page_obj": page_obj
        })


    else:

        # PAGINATOR
        posts = Post.objects.all().order_by('-id')
        paginator = Paginator(posts, 10) # test Paginator with 10 per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # TDL check with AnonymousUSer
        postslikedbyuser = Like.objects.filter(likedby=user).values_list('postid', flat=True)
        
     
        return render(request, "network/index.html", {
            # Passing all posts from database (with latest first) to display them later
            "posts": posts,
            "page_obj": page_obj,
            "postslikedbyuser": postslikedbyuser
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

    # Check if the users wants to follow or unfollow / post_request
    if request.method == "POST":
        if 'follow' in request.POST:
            
            # Same as get method 
            # Does the user exist?
            try: 
                user_profiled = User.objects.filter(username=username)

                user_profiled_id = user_profiled.values_list('id', flat=True)
                user_profiled_id = user_profiled_id[0]

                # Get this user's posts WITH PAGINATOR
                user_posts = Post.objects.filter(userid=user_profiled_id).order_by('-id')
                paginator = Paginator(user_posts, 10) # test Paginator with 10 per page
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
            
                # Count the amount of followers for this user
                amount_of_followers = Follower.objects.filter(followed=user_profiled_id).count()

                # Count how many people this user is following
                amount_of_following = Follower.objects.filter(follower=user_profiled_id).count()

                # Checking the name of who is logged in
                user_logged_in = request.user.id

                # Checking if user_logged_in is following user in profile
                isfollowing = Follower.objects.filter(followed=user_profiled_id,follower=user_logged_in).count()

                # ADD ENTRY To FOLLOWER MODEL
                followed = User.objects.filter(id=user_profiled_id)
                followed = followed[0]
                follower = User.objects.filter(id=user_logged_in)
                follower = follower[0]
                follow = Follower(followed=followed,follower=follower)
                follow.save()
                
                # Reload Followers after the change in Model
                amount_of_followers = Follower.objects.filter(followed=user_profiled_id).count()
                amount_of_following = Follower.objects.filter(follower=user_profiled_id).count()
                isfollowing = Follower.objects.filter(followed=user_profiled_id,follower=user_logged_in).count()

                return render(request, "network/profile.html", {
                            "username": username,
                            "user_profiled": user_profiled,
                            "user_profiled_id": user_profiled_id,
                            "amount_of_followers": amount_of_followers,
                            "amount_of_following": amount_of_following,
                            "user_logged_in": user_logged_in,
                            "isfollowing": isfollowing,
                            "user_posts": user_posts,
                            "post_request": "follow",
                            "page_obj": page_obj
                        })

            # If not, display page without posts
            except IndexError:
                return render(request, "network/missingprofile.html", {
                            "username": username,
                        })

        elif 'unfollow' in request.POST:
            
            # Same as get method
            # Does the user exist?
            try: 
                user_profiled = User.objects.filter(username=username)

                user_profiled_id = user_profiled.values_list('id', flat=True)
                user_profiled_id = user_profiled_id[0]

                # Get this user's posts WITH PAGINATOR
                user_posts = Post.objects.filter(userid=user_profiled_id).order_by('-id')
                paginator = Paginator(user_posts, 10) # test Paginator with 10 per page
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

                # Count the amount of followers for this user
                amount_of_followers = Follower.objects.filter(followed=user_profiled_id).count()

                # Count how many people this user is following
                amount_of_following = Follower.objects.filter(follower=user_profiled_id).count()

                # Checking the name of who is logged in
                user_logged_in = request.user.id
                user_logged_in = int(user_logged_in)

                # Checking if user_logged_in is following user in profile
                isfollowing = Follower.objects.filter(followed=user_profiled_id,follower=user_logged_in).count()

                # DELETE ENTRY FROM FOLLOWER MODEL
                followed = User.objects.filter(id=user_profiled_id)
                followed = followed[0]
                follower = User.objects.filter(id=user_logged_in)
                follower = follower[0]
                follow = Follower.objects.filter(followed=followed,follower=follower)
                follow.delete()

                # Reload Followers after the change in Model
                amount_of_followers = Follower.objects.filter(followed=user_profiled_id).count()
                amount_of_following = Follower.objects.filter(follower=user_profiled_id).count()
                isfollowing = Follower.objects.filter(followed=user_profiled_id,follower=user_logged_in).count()

                return render(request, "network/profile.html", {
                            "username": username,
                            "user_profiled": user_profiled,
                            "user_profiled_id": user_profiled_id,
                            "amount_of_followers": amount_of_followers,
                            "amount_of_following": amount_of_following,
                            "user_logged_in": user_logged_in,
                            "isfollowing": isfollowing,
                            "user_posts": user_posts,
                            "post_request": "unfollow",
                            "page_obj": page_obj
                        })

            # If not, display page without posts
            except IndexError:
                return render(request, "network/missingprofile.html", {
                            "username": username,
                        })


    # GET method:
    else:
        # Does the user exist?
        try: 
            user_profiled = User.objects.filter(username=username)

            user_profiled_id = user_profiled.values_list('id', flat=True)
            user_profiled_id = user_profiled_id[0]

            # Get this user's posts WITH PAGINATOR
            user_posts = Post.objects.filter(userid=user_profiled_id).order_by('-id')
            paginator = Paginator(user_posts, 10) # test Paginator with 10 per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            # Count the amount of followers for this user
            amount_of_followers = Follower.objects.filter(followed=user_profiled_id).count()

            # Count how many people this user is following
            amount_of_following = Follower.objects.filter(follower=user_profiled_id).count()

            # Checking the name of who is logged in
            user_logged_in = request.user.id

            # Checking if user_logged_in is following user in profile
            isfollowing = Follower.objects.filter(followed=user_profiled_id,follower=user_logged_in).count()

            return render(request, "network/profile.html", {
                        "username": username,
                        "user_profiled": user_profiled,
                        "user_profiled_id": user_profiled_id,
                        "amount_of_followers": amount_of_followers,
                        "amount_of_following": amount_of_following,
                        "user_logged_in": user_logged_in,
                        "isfollowing": isfollowing,
                        "user_posts": user_posts,
                        "page_obj": page_obj
                    })

        # If not, display page without posts
        except IndexError:
            return render(request, "network/missingprofile.html", {
                        "username": username,
                    })

@login_required(login_url='login')
def following(request):

    # Checking the name of who is logged in
    user_logged_in = request.user.id

    # Check who this user is following:
    isfollowing = Follower.objects.filter(follower=user_logged_in)
    isfollowingids = Follower.objects.filter(follower=user_logged_in).values_list('followed',flat=True)

    
    # PAGINATOR
    # Filter posts made only by people followed
    posts = Post.objects.filter(userid__in=isfollowingids).order_by('-id')
    paginator = Paginator(posts, 10) # test Paginator with 10 per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, "network/following.html", {
       # Passing all posts from database (with latest first) to display them later
        "posts": posts,
        "isfollowing": isfollowing,
        "isfollowingids": isfollowingids,
        "user_logged_in": user_logged_in,
        "page_obj": page_obj
    })

@csrf_exempt
@login_required(login_url='login')
def editpost(request, postid, postchangedvalue):
    # Query for request post
   
    try:
        post = Post.objects.get(userid=request.user, pk=postid)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == 'PUT':
        post.post = postchangedvalue
        post.save()
        return HttpResponse(status=204)
    
    else:
        return JsonResponse({
            "error": "Not allowed"
        }, status=400)

@csrf_exempt
@login_required(login_url='login')
def addlike(request, postid):
    # Query for request post
   
    try:
        post = Post.objects.get(userid=request.user, pk=postid)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == 'PUT':
        post.likes = post.likes + 1
        post.save()
        # Query for entry in LIKE Model
        likedentry = Like(likedby=request.user, postid_id=postid)
        # Add entry to DB
        likedentry.save()
        return HttpResponse(status=204)
    
    else:
        return JsonResponse({
            "error": "Not allowed"
        }, status=400)

@csrf_exempt
@login_required(login_url='login')
def deletelike(request, postid):
    # Query for request post
   
    try:
        post = Post.objects.get(userid=request.user, pk=postid)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == 'PUT':
        post.likes = post.likes - 1
        post.save()
        # Query for entry in LIKE Model
        likedentry = Like.objects.get(likedby=request.user, postid=postid)
        # Delete entry from DB
        likedentry.delete()
        return HttpResponse(status=204)
    
    else:
        return JsonResponse({
            "error": "Not allowed"
        }, status=400)

    
    





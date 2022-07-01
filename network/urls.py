
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/<str:username>", views.profile_page, name="profile_page"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("following", views.following, name="following"),
    path("register", views.register, name="register"),
    
    # API routes
    path("post/<int:postid>/<str:postchangedvalue>", views.editpost, name="editpost"),
]

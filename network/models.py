from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"User number '{self.id}' is '{self.username}'. Last connexion: {self.last_login}."

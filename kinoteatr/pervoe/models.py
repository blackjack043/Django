from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=2000)

class Film(models.Model):
    film = models.CharField(max_length=20)
    src = models.CharField(max_length=200)
    genre = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)

class LK(models.Model):
    user = models.CharField(max_length=200)
    film_name = models.CharField(max_length=200)
    ryad = models.CharField(max_length=20)
    mesto = models.CharField(max_length=20)

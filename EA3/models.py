"""
Definition der Model-Klassen
File: models.py
"""

from django.db import models

class MovieCategory(models.Model):
    """ Definition einer MovieCategory"""
    category = models.CharField(max_length=32)

class Movie(models.Model):
    """ Definition der Klasse Movie """
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    title_text = models.CharField(default='No title yet', max_length=100)
    description_text = models.CharField(default='No description yet', max_length=400)
    actors_text = models.CharField(default='No actors yet', max_length=200)
    posterPath = models.CharField(default='defaultposter.jpg', max_length=256)
    year = models.IntegerField(default=0)
    voteCount = models.IntegerField(default=0)

class User(models.Model):
    """ Definition der Klasse User (wird aktuell nicht verwendet) """
    name_text = models.CharField(max_length=32)
    email_text = models.CharField(max_length=100)

class Votes(models.Model):
    """ Definition der Klasse Votes """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now=True)
 
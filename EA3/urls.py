"""
Defiert die URL-Umleitungen für die EA3-App
File: urls.py
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('summary.html', views.getVoteSummary, name='VoteSummary'),
    path('<int:movieId>', views.getMovieTitle, name='MovieTitle'),
    path('', views.Home.as_view(), name='home'),
]
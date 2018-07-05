"""
Definition der Model-Klassen
File: Views.pyFile
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.http import Http404

from .models import Movie

class Home(TemplateView):
    """ View: Wird fuer die Anmeldung verwendet"""
    template_name = 'index.html'

def EA3(request):
    """ View: Nur zum Test"""
    if(request.GET.get('btnVote')):
        movieId = int(request.GET.get('movieIdInput'))
        return HttpResponse("Die Id %s " % movieId)

def getVoteSummary(request):
    """ View: getVoteSummary"""
    context = {
        'Movies': Movie.objects.order_by('-voteCount'),
    }
    return render(request, 'summary.html', context)

def index(request):
    """ View: Standardview"""
    if(request.GET.get('btnVote')):
        movieId = int(request.GET.get('movieIdInput'))
        # Aktuelles Movie-Objekt holen
        movie = Movie.objects.get(id=movieId)
        # Vote-Eigenschaft + 1
        movie.voteCount += 1
        movie.save()
    context = {
        'Movies': Movie.objects.all(),
        }
    return render(request, 'index.html', context)


def getMovieTitle(request, movieId):
    """ View: Ausgabe des Filmtitels"""
    response = "Der Film heißt: %s."
    try:
        title = Movie.objects.get(pk=movieId).title_text
    except:
        raise Http404("Diesen Film kennen wir nicht.")
    return HttpResponse(response % title)

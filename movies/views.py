from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies' : [
        {
            'id':5,
            'title' : 'Jaws',
            'year' : 1699

        },
        {
            'id':6,
            'title' : 'Jaws',
            'year' : 1899

        },
        {
            'id':7,
            'title' : 'Jaws',
            'year' : 1999

        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Hello world home")
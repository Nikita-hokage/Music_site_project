from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render
from .forms import AddJanrF, AddSongF, AddAuthorF
from .models import Janr, Author, Song


def mainstr(request):
    janr = Janr.objects.all()
    return render(request, 'pages/mainpage.html', {"janrs":janr})


# def janrGetName(request, name):
#     if Janr.objects.get(name):
#         data = {
#         "janr": name,
#         "description": Janr[name]
#     }
#         return render(request, 'pages/second.html', context=data)
#     else:
#         return HttpResponseRedirect('404')

def getnotFound(request):
    return render(request, 'pages/404.html')


def add_page(request):
    if request.method == 'POST':
        form = AddJanrF(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponseRedirect('404')
    else:
        form = AddJanrF()
    return render(request, 'pages/AddStr.html', {'form': form})


def add_song(request):
    if request.method == 'POST':
        form = AddSongF(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponseRedirect('404')
    else:
        form = AddSongF()
    return render(request, 'pages/Song.html', {"form": form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorF(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponseRedirect('404')
    else:
        form = AddAuthorF()
    return render(request, 'pages/author.html', {"form": form})


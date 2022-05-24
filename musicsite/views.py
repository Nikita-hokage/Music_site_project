from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render
from musicsite.forms import AddJanrF, AddSongF, AddAuthorF
from musicsite.models import Janr, Author, Song


def mainstr(request):
    return render(request, 'pages/mainpage.html')


# def janrGetName(request, name):
#     if janrs.get(name):
#         data = {
#         "janr": name,
#         "description": janrs[name]
#     }
#         return render(request, 'pages/secondpage.html', context=data)
#     else:
#         return HttpResponseRedirect('404')
#
#def getnotFound(request):
#    return render(request, 'pages/404.html')


def add_page(request):
    if request.method == 'POST':
        form = AddJanrF(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
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
                print('something went wrong')
    else:
        form = AddSongF()
    return render(request, 'page/Song.html', {"form": form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorF(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddAuthorF()
    return render(request, 'page/Song.html', {"form": form})


def get_teams(request):
    janr = Janr.objects.all()
    return render(request, 'mainpage/getTeams.html', {"janr": janr})

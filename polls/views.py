from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string

janrs = {'punk': 'punk is type'}

def mainstr(request):
    return HttpResponse(render_to_string('polls/structure.html'))

def janrGetName(request, name):
    if janrs.get(name):
        return HttpResponse(janrs[name])
    else:
        return HttpResponseRedirect('404')

def getnotFound(request):
    return HttpResponse(render_to_string('polls/404.html'))
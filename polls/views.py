from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

janrs = {'Punk-rock': 'punk is type',
         'alternative rock': "жанр",
         "Art-rock": "aa",
         "Beat": "ads",
         "Garage rock": "roooock",
         "Glam rock": "Britan",
         "Gothic rock":"0",
}

def mainstr(request):
    data = {
        "janrs":janrs.keys()
    }
    return render(request, 'polls/structure.html', context=data)

def janrGetName(request, name):
    if janrs.get(name):
        data = {
        "janr": name,
        "description": janrs[name]
    }
        return render(request, 'polls/second.html', context=data)
    else:
        return HttpResponseRedirect('404')

def getnotFound(request):
    return render(request, 'polls/404.html')
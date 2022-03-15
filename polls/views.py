from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

janrs = {'punk': 'punk is type',
         'alternative': "жанр"
}

def mainstr(request):
    return render(request, 'polls/structure.html',)

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
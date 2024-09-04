from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):    
    if request.method == "POST":
        return HttpResponse("We are POSTING Baby!")
    elif request.method == "GET":
        return HttpResponse(request.method)
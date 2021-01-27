from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Yo, you are in the polls app!!!")

def frog(request):
    return HttpResponse('ducktales')
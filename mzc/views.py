from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indexpage(request):
    return HttpResponse("welcome to my index page")
def contactpage(request):
    return HttpResponse("welcome to contact page")
def homepage(request):
    return HttpResponse("welcome to my home page")    
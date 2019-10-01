from django.shortcuts import render
from django.http import HttpResponse
from .forms import Facultyform
# Create your views here.
def indexpage(request):
    return render(request,'index.html')
def contactpage(request):
    return render(request,'contact.html')
def homepage(request):
    return render(request,'home.html')  
def facultypage(request):
    form=Facultyform()
    return render(request,'faculty.html',{'form':form})     
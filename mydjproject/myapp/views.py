from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,"home.html")
def aboutpage(request):
    return render(request,'about.html')
def conatactpage(request):
    return render(request,'contact.html')

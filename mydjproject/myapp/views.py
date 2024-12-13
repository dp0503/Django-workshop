from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
from .forms import studentform
# Create your views here.

def homepageview(request):
    return render(request,'home.html')

def formpageview(request):
    return render(request,'form.html')

def formpageprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    return render(request,"ans.html",{'mya':a,'myb':b,'sum':c})

def addstudent(request):
    if request.method == "GET":
        context = {'form':studentform()}
        return render(request,'add.html',context)
    elif request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(addstudent)
        else:
            return render(request,'add.html',{'form':form})
def displaystudent(request):
    dbdata = student.objects.all()
    context = {'mydata':dbdata}
    return render(request,'display.html',context)

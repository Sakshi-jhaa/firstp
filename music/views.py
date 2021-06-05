from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home.html',{"name":"Sakshi"})
#    return HttpResponse("<h1>Hello</h1>")
def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2
    return render(request,'result.html',{'result':res})
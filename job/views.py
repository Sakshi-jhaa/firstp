from django.shortcuts import render,redirect
from .models import Application
from django.contrib import messages
# Create your views here.
def portal(request):
    app=Application.objects.all()
    key=Application.objects.filter(Location='Hubli',salary=50)
    return render(request,"portal.html",{'app':app,'key':key})
    

def apply(request):
    if request.method=='POST':
        job_role=request.POST['job_role']
        Qualification=request.POST['Qualification']
        Specification=request.POST['Specification']
        Location=request.POST['Location']
        salary=request.POST['salary']
        apply_date=request.POST['apply_date']
        a=Application(job_role=job_role,Qualification=Qualification,Specification=Specification,Location=Location,salary=salary,apply_date=apply_date)
        a.save()
        messages.info(request,'Applied Succesfully!')
        return redirect('/')
    else:
        return render(request,'apply.html')

# def query(request):
#     context={
#     'l':Application.objects.filter(Location='Hubli',salary=50),
#     's':len(Application.objects.filter(Location='Hubli',salary=50))
#     }
#     return render(request,'job/query.html',context)
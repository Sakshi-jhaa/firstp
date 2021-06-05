from django.shortcuts import render,redirect
from .models import Donation
# Create your views here.
def bookstore(request):
    donors=Donation.objects.all()
    return render(request,"bookstore.html",{'donors':donors})

def donate(request):
    if request.method=='POST':
        Number_of_items=request.POST['Number_of_items']
        Donor_name=request.POST['Donor_name']
        Items=request.POST['Items']
        cash=request.POST['cash']
        donation_date=request.POST['donation_date']
        a=Donation(Number_of_items=Number_of_items,Donor_name=Donor_name,Items=Items,cash=cash,donation_date=donation_date)
        a.save()
        return redirect('/')
    else:
        return render(request,'donate.html')
    


    
    
    
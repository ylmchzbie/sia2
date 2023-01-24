from django.shortcuts import render
from pos_aircon.models import customer_details
from django.contrib import messages

# Create your views here.

def customerDisplay(request):
    results=customer_details.objects.all()
    return render(request, "index.html", {"customer_details":results})

def newCustomer(request):
    if request.method=="POST":
        if request.POST.get('customerName') and request.POST.get('customerPhone') and request.POST.get('customerEmail') and request.POST.get('customerAddress'):
            saveCustomer = customer_details()
            saveCustomer.customerName=request.POST.get('customerName')
            saveCustomer.customerPhone=request.POST.get('customerPhone')
            saveCustomer.customerEmail=request.POST.get('customerEmail')
            saveCustomer.customerAddress=request.POST.get('customerAddress')
            saveCustomer.save()
            messages.success(request, "Customer Record" + saveCustomer.customerName + "'s details is recorded!")
            return render(request,"create.html")
        else:
            return render(request,"create.html")
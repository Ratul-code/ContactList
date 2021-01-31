from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    param={'contacts':[i for i in Contact.objects.all()]}
    return render(request,"contactlist/contacthome.html",param)

def addcontact(request):
    if request.method=="POST":
        if request.POST.get('name')!='' and request.POST.get('relation')!='':
            contact=Contact(
                name=request.POST.get('name'),
                relation=request.POST.get('relation'),
                phone_no=request.POST.get('phone_no'),
                email=request.POST.get('email'),
                address=request.POST.get('address')
                )
            contact.save()
            return redirect("/")
        else:
            raise ValueError("sorry")
    
    return render(request,'contactlist/contactlist.html')
def profile(request,pk):
    contact=Contact.objects.get(id=pk)
    return render(request,"contactlist/profile.html",{"contact":contact})

def editcontact(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=="POST":
        contact.name=request.POST.get("name")
        contact.relation=request.POST.get("relation")
        contact.phone_no=request.POST.get("phone_no")
        contact.email=request.POST.get("email")
        contact.address=request.POST.get("address")
        contact.save()
        return redirect("/")
    params={"contact":contact}
    return render(request,'contactlist/edit.html',params)


def delete(request,pk):
    contact=Contact.objects.get(id=pk)
    contact.delete()
    return redirect("/")
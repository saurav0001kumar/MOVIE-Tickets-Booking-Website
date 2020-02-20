from django.shortcuts import render,redirect
from django.http import HttpResponse
from movieapp.models import movies
from movieapp.models import movies2,reg
from movieapp.form import regForm
from movieticket import settings
# Create your views here.
def index(request):
    m = movies2.objects.all()
    
    return render(request,'index.html',{'m':m})

def upcoming(request):
    m1 = movies.objects.all()
    return render(request,'upcoming.html',{'m':m1})

def login(request):
    return render(request,'loginform.html')

def signup(request):
    if request.method=="POST":
        form=regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/booked")
    else:
        form=regForm()
        return render(request,'signup.html',{'form':form})
    
    
    
    

def booked(request):
    ob=reg.objects.all()
    return render(request,'booked.html',{'ob':ob})

def about(request):
    return render(request,'Untitled-1.html')

def details(request,id):
    d=movies2.objects.get(id=id)
    return render(request,'details.html',{'d':d})

def updetails(request,id):
    d=movies.objects.get(id=id)
    return render(request,'updetails.html',{'d':d})

def aboutmore(request):
    return render(request,'about.html')

from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    data={
        'studentsData':Students.objects.all()
    }
    return render(request,'index.html',data)

    
def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        Students.objects.create(name=name,address=address)
        return redirect('/')

    else:
        return redirect('/')

def delete(request,id):
        Students.objects.get(id=id).delete()
        return redirect('/')

def edit(request,id):
    if request.method=='POST':
        sobj=Students.objects.get(id=id)
        sobj.name=request.POST.get('name')
        sobj.address=request.POST.get('address')
        sobj.save()
        return redirect('/')
    else:
        data={
             'studentsData': Students.objects.get(id=id),
        
        }
        return render(request,'edit.html',data)





def teacher(request):
    data={
        'teacherdata':Teacher.objects.all()
    }
    return render(request,'addteacher.html',data)

def addteacher(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        Teacher.objects.create(name=name,address=address)
        return redirect('teacher')

    else:
        return render(request,'addteacher.html')
    


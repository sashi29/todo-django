from django.shortcuts import render,redirect
from .models import Todolist
# Create your views here.
def home(request): 
    data=Todolist.objects.all()
    context={"data":data}
    return render(request,'home.html',context) 

def addtask(request): 
    if request.method=="POST": 
        task=request.POST["addtask"] 
        if task!="":
            todo=Todolist(name=task) 
            todo.save() 
        else: 
            return redirect("/") 
    return redirect("/") 

def changestatus(request,id): 
    task=Todolist.objects.get(id=id) 
    if task.status==True: 
        task.status=False 
    else: 
        task.status=True 
    task.save()
    return redirect("/") 

def delete(request,id): 
    task=Todolist.objects.get(id=id) 
    task.delete() 
    return redirect("/")
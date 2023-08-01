from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Task

# Create your views here.
def index(request):
    name=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date= request.POST.get('date','')
        task=Task(task=name,priority=priority,date=date)
        task.save()
        return redirect('/')

    return render(request, 'home.html',{'name':name})


def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        task.save()
        return redirect('/')

    return render(request,'update.html',{'f':f,'task':task})
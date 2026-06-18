from django.shortcuts import render,redirect
from .models import TaskModel
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = TaskModel.objects.filter(Q(host = request.user) & Q(is_delete = False) & (Q(title__icontains = q) | Q(desc__icontains = q)))
        if len(data) == 0:
            messages.error(request,'No Data Found')
            # return redirect(home)
    else:
        data = TaskModel.objects.filter(host = request.user,is_delete = False)
    
    if request.method =='POST':
        TaskModel.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        host = request.user
        )
    return render(request,'home.html',{'data':data})

def trash(request):
    data = TaskModel.objects.filter(host = request.user,is_delete = True)
    return render(request,'trash.html',{'data':data})

def delete(request,id):
    data = TaskModel.objects.get(id=id)
    data.is_delete = True
    data.save()
    return redirect('home')

def trestore(request,pk):
    data = TaskModel.objects.get(id=pk)
    data.is_delete = False
    data.save()
    return redirect(home)

def deleteall(request):
    data = TaskModel.objects.filter(host = request.user,is_delete = False)
    for i in data:
        i.is_delete = True
        i.save()
    return redirect('trash')    

def trestoreall(request):
    data = TaskModel.objects.filter(host = request.user,is_delete = True)
    for i in data:
        i.is_delete = False
        i.save()
    return redirect('home') 

# permanently delete data
def tdeleteall(request):
    data = TaskModel.objects.filter(host=request.user,is_delete=True)
    data.delete()
    return redirect('trash')

# permanently delete only that task
def tdelete(request, pk):
    data = TaskModel.objects.get(id=pk)
    data.delete()
    return redirect('trash')

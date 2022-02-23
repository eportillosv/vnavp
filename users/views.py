from ast import If
import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UsersForm

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

def usuario(request):
    users = User.objects.all()
    return render(request, 'page/user.html', {'users': users})

def crear(request):
    forms = UsersForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
        forms.save()
        return redirect('usuario')
    return render(request, 'page/crear.html', {'forms':forms})

def edit(request, id):
    users = User.objects.get(id=id)
    forms = UsersForm(request.POST or None, request.FILES or None, instance=users)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('usuario')
    return render(request, 'page/edit.html', {'forms': forms})

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('usuario')

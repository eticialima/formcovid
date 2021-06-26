from django.shortcuts import render, redirect
from app.forms import cadastroForm
from app.models import cadastro
from django.core.paginator import Paginator 
# Create your views here.
def home(request):
    return render(request, 'inicio.html')

def index(request):
    data = {}    
    search = request.GET.get('search') 
    if search:
        data['db'] = cadastro.objects.filter(user_name__icontains=search)
    else:
        data['db'] = cadastro.objects.all()
     
    return render(request, 'index.html', data)

def form(request):
    data={}
    data['form'] = cadastroForm()
    return render(request, 'form.html', data)

def create(request):
    form = cadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

def view(request, pk):
    data = {}
    data['db'] = cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = cadastro.objects.get(pk=pk)
    data['form'] = cadastroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = cadastro.objects.get(pk=pk)
    form = cadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('index')

def delete(request, pk):
    db = cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('index')

 
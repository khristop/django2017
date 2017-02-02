from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'base.html', {"titulo":"inicio"})

def principal( request):
    return render(request, 'inicio.html',{"titulo":"principal"})

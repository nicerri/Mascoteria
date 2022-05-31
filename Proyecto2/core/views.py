from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/Index.html')

def Suscribirse(request):
    return render(request,'core/Suscribirse.html')

def OtrosPerros(request):
    return render(request,'core/OtrosPerros.html')

def IdPerro(request):
    return render(request,'core/Idperro.html')

def Donaciones(request):
    return render(request,'core/Donaciones.html')

def CorreasPerros(request):
    return render(request,'core/CorreasPerros.html')

def Contacto(request):
    return render(request,'core/Contacto.html')

def BandanasPerros(request):
    return render(request,'core/BandanasPerros.html')

def BandanasGatos(request):
    return render(request,'core/BandanasGatos.html')


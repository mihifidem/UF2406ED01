from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'producto/home.html', {"mensaje": "hola desde el frontend"})
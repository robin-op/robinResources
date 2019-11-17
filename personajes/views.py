from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def link(request):
    return render(request, 'personajes/link.html')
def cloud(request):
    return render(request, 'personajes/Cloud.html')
def corrin(request):
    return render(request, 'personajes/Corrin.html')
def ike(request):
    return render(request, 'personajes/Ike.html')
def inkling(request):
    return render(request, 'personajes/Inkling.html')
def joker(request):
    return render(request, 'personajes/Joker.html')
def lucina(request):
    return render(request, 'personajes/Lucina.html')
def marth(request):
    return render(request, 'personajes/Marth.html')
def pit(request):
    return render(request, 'personajes/Pit.html')
def roy(request):
    return render(request, 'personajes/Roy.html')
def chrom(request):
    return render(request, 'personajes/Chrom.html')
def robin(request):
    return render(request, 'personajes/Robin.html')
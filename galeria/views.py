from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def pesquisa(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'input' in request.GET:
        input_da_pesquisa = request.GET['input']
        if input_da_pesquisa:
            fotografias = fotografias.filter(nome__icontains=input_da_pesquisa)

    return render(request, 'galeria/pesquisa.html', {'cards': fotografias})
from django.urls import path
from galeria.views import index, imagem, pesquisa

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('pesquisa', pesquisa, name='pesquisa'),
]
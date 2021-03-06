from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
from .forms import PruebaForm

#import models
from .models import Prueba
# Create your views here.


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumeFoundtionView(TemplateView):
    template_name = 'home/resume_foundation.html'




class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'LISTA'
    queryset = ['0', '10', '20', '30']
    

class ListaPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = "lista"


    def __str__(self):
        return self.titulo + ' ' + self.subtitulo


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    seccess_url = '/'
    

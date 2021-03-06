from django.contrib import admin
from django.urls import path, re_path, include

from . import views
app_name = 'departamento_app'
urlpatterns = [
    path(
        'departamento_lista/',
        views.DepartamentoListView.as_view(), 
        name = 'departamento_list'), 

    path('new_departamento/',
    views.NewDepartamentoView.as_view(), 
    name = 'nuevo_departamento'), 
]

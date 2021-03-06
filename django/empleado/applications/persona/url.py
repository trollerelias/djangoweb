from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name = 'persona_app'



urlpatterns = [
    path(
        '',
        views.InicioView.as_view(), 
        name='inicio'
        ),

    path(
        'lista_empleados_admin',
        views.ListaEmpleadosAdmin.as_view(), 
        name='empleados_admin'
        ),
    

    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados-all'
        ),


    path(
        'listar-by-area/<shorname>/',
        views.ListByAreaEmpleados.as_view(),
        name='emple'
        ), 


    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()), 
    path('listar-habilidades-empleados/<pk>', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailViewDetailView.as_view(),
        name='empleado_detail'
        ),  

    path('add-empleado/', 
    views.EmpleadoCreateView.as_view(),
    name='empleado_add'
    ), 
    
    path(
        'success/',
        views.SuccessView.as_view(), 
        name='correcto'
        ),
     
     
   path(
        'update-empleado/<pk>',
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'),


    path(
        'delete-empleado/<pk>',
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'),
    

     



]
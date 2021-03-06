from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

class InicioView(TemplateView):
    template_name = 'inicio.html'



from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    #?page=2
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        
        palabra_clave = self.request.GET.get('kword', '')
        
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )

        
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    #?page=2
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

   
  
  


class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    

    def get_queryset(self):

        area = self.kwargs['shorname']


        lista = Empleado.objects.filter(
            departamento__name = area
    )
        return lista
 



class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'


    def get_queryset(self):
        print('HHHHHHHHHHHHHHHHH')
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )

        
        return lista




class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=6)
      
        return empleado.habilidades.all()





class EmpleadoDetailViewDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailViewDetailView, self).get_context_data(**kwargs)

        context['titulo'] = ' Empleado del mes'
        return context
    


class SuccessView(TemplateView):
    template_name = 'persona/success.html'



class EmpleadoCreateView(CreateView):
    
    template_name = "persona/add.html"

    model = Empleado

    fields = [
        'first_name',
        'last_name',
        'departamento',
        'job',
        'habilidades',
        'avatar',
    ]

    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    
    
    model = Empleado

    fields = [
        'first_name',
        'last_name',
        'departamento',
        'job',
        'habilidades',
        

    ]

    success_url = reverse_lazy('persona_app:empleados_admin')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('HHHHHHHHHHHHHHHHHHHHHHHHH')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)




class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


  

# Create your views here.

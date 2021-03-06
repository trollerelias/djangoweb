from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + ' ' + self.habilidad



class Empleado(models.Model):
    """modelo para empleados"""
    JOB_CHOICES = (
        ('0', 'contador'),
        ('2', 'administrador'),
        ('3' ,'economista'),
        ('4' ,'otro'),
    )



    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombre Completo',
        max_length=120,
        blank=True
        

    )
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Mis Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        



    def __str__(self):
        return str(self.id) + ' ' +self.first_name + ' ' + self.last_name

from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mis departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']

    def __str__(self):

        # return str(self.id) + ' ' +self.name + ' ' + self.shor_name
        # este me sirve por si quiero agregar el id y el nombre corto

        return self.name 
        
        
      

# -*- coding: utf-8 -*-
from django.db import models

class Todo(models.Model):
    nombre = models.CharField(
                'Nombre',
                max_length=200,
                help_text='Ingrese el nombre del proyecto',
                null=True,
                blank=True
                )

    class Meta:
        app_label = 'usuario'
        ordering = ('nombre', )


    def __unicode__(self):
        return self.nombre

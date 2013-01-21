# -*- coding: utf-8 -*-

from django.db import models

from usuario.models.todo import Todo

class Articulo(models.Model):
    fktodo = models.ForeignKey(Todo)
    tarea = models.TextField('Tarea', help_text='Descripción de la tarea')
    fecha = models.DateField()
    
    class Meta:
        app_label = 'usuario'
        verbose_name = u'Todo Tarea'
        verbose_name_plural = u'Todo Tareas'

    def __unicode__(self):
        return u'%s | %s' % (self.fktodo, self.tarea)

    
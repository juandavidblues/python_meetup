from django.db import models

class Mensaje(models.Model):
    titulo = models.CharField(max_length=100,verbose_name='Titulo Mensaje',blank=False,null=True)
    autor = models.CharField(max_length=100,verbose_name='Autor',blank=False,null=True)
    mensaje = models.TextField(verbose_name='Mensaje',blank=False,null=True)
    destinatario = models.CharField(max_length=100,verbose_name='Destinatario',blank=True,null=True)

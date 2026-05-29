from django.db import models
from datetime import date


class todo(models.Model):
    titulo = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(verbose_name="Data de Entrega",null=False, blank=False)
    datafinal = models.DateField(null=True)

    class Meta:
        ordering = ["data_entrega"]

    def mark_has_complete(self):
        if not self.datafinal:
            self.datafinal = date.today() 
            self.save()
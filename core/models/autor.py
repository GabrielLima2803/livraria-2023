from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(blank=True, max_length=255)
    def __str__(self):
        return f"{self.id} - {self.nome}"
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
from django.db import models

class Livro(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=50)
    anoPublicacao = models.IntegerField()
    numeroPagina = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
    
class Meta:
    verbose_name = "Livro"
    

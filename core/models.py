from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_inicio = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.nome)
        
    class Meta:
        db_table = 'livro'
        
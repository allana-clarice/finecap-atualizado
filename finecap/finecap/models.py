from django.db import models

# Create your models here.
class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao

class Reserva(models.Model):
    cnpj = models.CharField(max_length=18)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=50)
    quitado = models.BooleanField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_empresa
"""modelagem de dados """
from django.db import models

class Taxi(models.Model):
    """
    Modelo que representa um táxi na aplicação.

    Atributos:
    - id: chave primária autoincrementada que identifica o táxi
    - plate: placa do táxi (máx. 10 caracteres)
    """
    id = models.AutoField('id', primary_key=True)
    plate = models.CharField('plate', max_length=10)

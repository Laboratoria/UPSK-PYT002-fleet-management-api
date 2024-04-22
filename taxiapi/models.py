"""modelagem de dados """
from django.db import models

class Taxis(models.Model):
    """dados que contém na tabela do banco de dados"""
    id = models.AutoField('id', primary_key=True)
    plate = models.CharField('plate', max_length=10)
    
    def __str__(self):
        return f"Id: {self.id}, Plate: {self.plate}"

#class Trajetoria(models.Model):
  #  """dados que contém na tabela de banco de dados"""
   # id = models.AutoField()
   # taxi_id = models.ForeignKey(Taxis, on_delete=models.CASCADE)
    #date = models.DateTimeField(auto_now_add=True)
    #latitude = models.FloatField(max_length=15)
    #longitude = models.FloatField(max_length=15)

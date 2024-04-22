from django.db import models

class Taxis(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10)

class Trajetoria(models.Model):
    id = models.AutoField()
    taxi_id = models.ForeignKey(Taxis, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(max_length=15)
    longitude = models.FloatField(max_length=15)


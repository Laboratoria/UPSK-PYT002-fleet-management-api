"""Módulo contendo os serializers para a API da aplicação taxi"""

from rest_framework import serializers
from taxi import models

class TaxiSerializer(serializers.ModelSerializer):
    """Serializador para objetos da classe Taxi do modelo Taxi"""
    class Meta:
        """ Classe Meta para definir metadados para o TaxiSerializer. 
        Aqui, configuramos o modelo a ser serializado (models.Taxi) e os campos que devem ser 
        incluídos na serialização. """
        model = models.Taxi
        fields = '__all__'
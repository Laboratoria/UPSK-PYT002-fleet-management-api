
"""Este módulo contém as views da API para a aplicação de táxi."""
from rest_framework import viewsets
from taxi import serializers 
from taxi import models

class TaxiViewSet(viewsets.ModelViewSet):
    """Viewset que fornece endpoints para operações CRUD na entidade Taxi.
    
    Atributos:
    serializer_class: Classe de serialização utilizada para transformar objetos Taxi em dados JSON.
    queryset: Queryset que retorna todos os objetos da classe Taxi.
    """
    serializer_class = serializers.TaxiSerializer
    queryset = models.Taxi.objects.all()

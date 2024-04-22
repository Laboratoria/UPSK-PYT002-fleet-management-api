
"""views da api"""
from django.shortcuts import render

def index(request):
    """função que renderisa o arquivo html"""
    return render(request,"taxis/lista_taxis.html")

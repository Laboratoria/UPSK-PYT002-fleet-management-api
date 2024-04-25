"""urls da api"""

from django.urls import path
from .views import TaxiViewSet

urlpatterns = [
    path('taxi', TaxiViewSet.as_view(), name='taxi-list')
]

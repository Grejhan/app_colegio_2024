from django.urls import path
from .views import ControlInicial

urlpatterns = [
    path('inicio/', view=ControlInicial)
] 
from django.urls import path
from .views import ControlInicial,CursosContorl

urlpatterns = [
    path('inicio/', view=ControlInicial),
    path('cursos/', view=CursosContorl.as_view())
] 
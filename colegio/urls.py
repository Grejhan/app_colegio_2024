from django.urls import path
from .views import ControlInicial,CursosContorl,CursoControlador,CalificacionsControler

urlpatterns = [
    path('inicio/', view=ControlInicial),
    path('cursos/', view=CursosContorl.as_view()),
    path('curso/<int:id>', view=CursoControlador.as_view()),
    path('calificacion/', view=CalificacionsControler.as_view())
] 
from django.urls import path
from .views import  DocenteRegistro,ControlDocente


urlpatterns = [
    path('docentes/', view=DocenteRegistro.as_view()),
    path('docente/<int:id>', view=ControlDocente)
] 
from django.urls import path
from .views import  DocenteRegistro,DocenteControler


urlpatterns = [
    path('docentes/', view=DocenteRegistro.as_view()),
    path('docente/<int:id>/', view=DocenteControler.as_view())
] 
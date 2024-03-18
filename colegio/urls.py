from django.urls import path
from .views import ( DocenteRegistro,
                    DocenteControler,
                    CrearCurso,
                    ListarCursosDocente,
                    ListarCalificaciones,
                    CalificarCursos, 
                    EstudianteRegistro)


urlpatterns = [
    path('docentes/', view=DocenteRegistro.as_view()),
    path('docente/<int:id>/', view=DocenteControler.as_view()),
    path('cursos/', view=CrearCurso.as_view()),
    path('cursos/<int:id>/docente/', view=ListarCursosDocente.as_view()),
    path('calificar/curso/<int:id>/', view=ListarCalificaciones),
    path('agregar-calificacion/curso/<int:id>/', view=CalificarCursos.as_view()),
    path('estudiante/', view=EstudianteRegistro.as_view()),
    path('estudiante/<int:id>/', view=EstudianteRegistro.as_view())
] 
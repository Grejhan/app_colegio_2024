from django.urls import path
from .views import ( DocenteRegistro,
                    DocenteControler,
                    CrearCurso,
                    CalificarCursos, 
                    EstudianteRegistro,
                    EstudianteControler,
                    ListarCalificaciones,
                    AgregarAlumnoCurso,
                    )


urlpatterns = [
    path('docentes/', view=DocenteRegistro.as_view()),
    path('docente/<int:id>/', view=DocenteControler.as_view()),
    path('cursos/', view=CrearCurso.as_view()),
    path('agregar-calificaciones/curso/<int:id>/', view=CalificarCursos.as_view()),
    path('estudiantes/', view=EstudianteRegistro.as_view()),
    path('estudiante/<int:id>/', view=EstudianteControler.as_view()),
    path('listar-calificaciones/', view=ListarCalificaciones.as_view()),
    path('alumno-curso/', view=AgregarAlumnoCurso.as_view())
    
]
    
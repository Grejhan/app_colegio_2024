from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import*
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from os import remove



@api_view(http_method_names=['GET','POST'])
def rutaInicial(request):
    return Response({
        'message':'Bienvendo al Api Colegio'
    })
class DocenteRegistro(APIView):
    def get(self, request):
        respuesta = Docente.objects.all()
        serializador = DocenteSerializer(instance=respuesta, many=True)
        return Response(data={
            'message':'Informacion del Docente',
            'content': serializador.data
        })
    def post(self, request):
        print(request.data)
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        serializador = DocenteSerializer(data=request.data)
        validacion = serializador.is_valid()
        if validacion:
            serializador.save()
            return Response(data={
                'message':'Docente Creado Exitosamente',
                'content': serializador.data
                
            })
        else:
            return Response(data={
                'message':'Error al crear al Docente',
                'content':serializador.errors
            })
        
class DocenteControler(APIView):
    def get(self, request, id):

        docente_encontrado = Docente.objects.filter(id=id).first()
        if not docente_encontrado:
            return Response(data={
                'message':'El docente no existe',
            })
        else:
            serializador = DocenteSerializer(instance=docente_encontrado)
            return Response(data={
                'message':'Docente encontrado',
                'content': serializador.data
            })
    
    def put(self, request, id):
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        docente_encontrado = Docente.objects.filter(id=id).first()
        if not docente_encontrado:
            return Response(data={
                'message':'El docente no existe',
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_anterior= docente_encontrado.foto.path

        serializador= DocenteSerializer(data=request.data)

        if serializador.is_valid():
            serializador.update(instance=docente_encontrado, 
                                validated_data=serializador.validated_data)
            
            remove(imagen_anterior)
            return Response(data ={
                'message': 'Docente actualizado exitosamente',
                'content': serializador.data
            })
        else:
            return Response(data={
                'message': 'Error al actualizar al Docente',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        docente_encontrado = Docente.objects.filter(id=id).first()
        if not docente_encontrado:
            return Response(data={
                'message': 'El docente no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        imagen_anterior= docente_encontrado.foto.path        
        Docente.objects.filter(id=id).delete()
        remove(imagen_anterior)
        return Response(data={
            'message':'El docente se elimino exitosamente'
        }, status=status.HTTP_204_NO_CONTENT)

class CrearCurso(APIView):
    def post(self, request):

        serializador = CursoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({
                'message': 'Curso agregado Exitosamente',
                'content': serializador.data

            }, status=status.HTTP_201_CREATED)  
        else:
            return Response({
                'message':'Error al guardar el curso',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class ListarCursosDocente(APIView):
    def get(self,resquest, id):

        curso_encontrado=Curso.objects.filter(docenteId=id).all()
        if not curso_encontrado:
            return Response({
                'message':'El docente no tiene cursos'
            })
        else:
            serializador = CursoSerializer(instance=curso_encontrado, many=True)
            return Response({
                'contet':serializador.data
            })

@api_view(http_method_names=['GET','POST','PUT'])
def ListarCalificaciones(request,id):
    calificacion_curso = Calificacion.objects.filter(cursoId=id).all()
    if not calificacion_curso:
        return Response({                                                            # en lista las calificaciones por cursoId = id
            'message':'El curso no tiene calificaicones',
            
        })
    else:
        serializador = CalificacionSerializer(instance=calificacion_curso, many=True)
        return Response({
            'content':serializador.data
        })
    
class CalificarCursos(APIView):
    def post(self,request,id):
        serializador = CalificacionSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response({
                'message':'calificaciones agregadas exitosamente',
                'content':serializador.data
            })
        else:
            return Response({
                'message':'Error al guardar calificaciones',
                'content':serializador.errors
            })

class EstudianteRegistro(APIView):
        
    def post(sefl, request):
        hasheo = make_password(request.data.get('password'))
        request.data['password'] = hasheo
        serializador = EstudianteSerializer(data=request.data)
        validacion=serializador.is_valid()
        serializador.save()
        if validacion:
            return Response(data={
                'message':'Estudiante creado exitosamente',
                'content': serializador.data
            })
        else:
            return Response(data={
                'message':'Error al crear estudiante',
                'content':serializador.errors
            })
        
    def get(self, request):
        estudiante_encontrado = Estudiante.objects.all()
        serializador = EstudianteSerializer(instance=estudiante_encontrado, many=True)
        if estudiante_encontrado:
            return Response(data={
                'mensage':'el estudiante si existe',
                'content': serializador.data
            })

class EstudianteControler(APIView):
    def get(self,request,id):
        estudiante_encontrado=Estudiante.objects.filter(id=id).first()
        if not estudiante_encontrado:
            return Response(data={
            'message':'El estudiante no existe'
            })
        else:
            serializador = EstudianteSerializer(instance=estudiante_encontrado)
            return Response(data={
                'message':'estudiante encontrado',
                'content': serializador.data
            })
        
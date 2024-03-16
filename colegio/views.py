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





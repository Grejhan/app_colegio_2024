from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import*
from rest_framework import status



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
        
@api_view(http_method_names=['PUT','DELETE'])       
def ControlDocente(self, request,id):
        docente_encontrado=Docente.objects.filter(id=id).first()
        if docente_encontrado:
            return Response(data={
                'message':'El docente no existe'
            })
        
        serializador = DocenteSerializer(data=request.data)
        if serializador.is_valid():
            actualizador =serializador.update(instance=docente_encontrado,
                                            validated_data=serializador.validated_data)
            return Response(data={
                'message':'Docente actualizado exitosamente'
            })
        else:
            return Response(data={
                'message':'error al actualizar docente',
                'content':serializador.erros
            })
        
def delete(self,request,id):
        docente_encontrado = Docente.objects.filter(id = id).first()
        if not docente_encontrado:
            return Response(data={
                'message':'El docente no existe'
            })
        Docente.objects.filter(id = id).delete()
        return Response(data={
            'message':'El docente se elimino exitosamente'
        })
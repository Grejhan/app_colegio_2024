from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Usuario
from .serializers import CursoSerializer
from rest_framework import status



@api_view(http_method_names=['GET','POST'])
def ControlInicial(request):
    return Response(data={
        'message':'Bienvenido a mi APi de Colegio'
    })

class CursosContorl(APIView):
    def get(self, request):
        resultado = Curso.objects.all()
        print(resultado)
        serializador = CursoSerializer(instance=resultado, many=True)
        return Response(data={
            'message':'Me hicieron get',
            'content':serializador.data
        })
    def post(self,request):
        print(request.data)
        serializador = CursoSerializer(data=request.data)
        validacion=serializador.is_valid()
        if validacion:
            serializador.save()
            return Response(data={
                'message':'Curso creado exitosamentre',
                'content': serializador.data
            }, status=status.HTTP_201_CREATED )
        else:
            return Response(data={
                'menssage':'Error al crear el curso',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class CursoControlador(APIView):
    def get(self, request, id):
            curso_encontrado = Curso.objects.filter(id = id).first()
            if not curso_encontrado:
                return Response(data={
                    'message':'No se encontro el curso'
                }, status=status.HTTP_404_NOT_FOUND)
            serializador = CursoSerializer(instance=curso_encontrado)
            return Response(data={
                    'content': serializador.data
                })
    def put(self, request, id):
            curso_encontrado = Curso.objects.filter(id = id).first()
            if not curso_encontrado:
                return Response(data={
                    'message':'No se encontro el curso'
                }, status=status.HTTP_404_NOT_FOUND)
            serializador = CursoSerializer(data = request.data)
            if serializador.is_valid():
                respuesta =  serializador.update(instance=curso_encontrado, validated_data=serializador.validated_data)
                print(respuesta)
                return Response (data={
                    'message':'El curso se actualizo corectamente'
                })

            else :
                return Response(data={
                    'message':'Error al actualizar el curso',
                    'content': serializador.errors
                }, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, id):
            curso_encontrado = Curso.objects.filter(id = id).first()
            if not curso_encontrado:
                return Response(data={
                    'message':'No se encontro el curso'
                }, status=status.HTTP_404_NOT_FOUND)
            
            Curso.objects.filter(id = id).delete()

            return Response(data={
                'message':'El curso se elimino exitosamente'
            }, status=status.HTTP_204_NO_CONTENT)
        

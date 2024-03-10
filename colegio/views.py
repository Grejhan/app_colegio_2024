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
                'content': ''
            }, status=status.HTTP_201_CREATED )
        else:
            return Response(data={
                'menssage':'Error al crear el curso',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
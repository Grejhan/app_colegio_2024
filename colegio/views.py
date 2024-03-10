from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response



@api_view(http_method_names=['GET','POST'])
def ControlInicial(request):
    return Response(data={
        'message':'Bienvenido a mi APi de Colegio'
    })



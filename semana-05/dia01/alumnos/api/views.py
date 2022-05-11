from logging import raiseExceptions
from django.http import JsonResponse

##### PARA TRABAJAR CON REST FRAMEWORK
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Alumno, Profesor
from .serializers import AlumnoSerializer, ProfesorSerializer

def index(request):
      return JsonResponse({
            'mensaje': 'Bienvenido a mi API'
      })

@api_view(['GET'])
def home(request):
      return Response({
            'status': 'Ok',
            'message': 'Bienvenidos a mi API REST (drf)'
      })
      
def alumnos(request):
      dataAlumnos = Alumno.objects.all()
      lstAlumnos = []
      for alumno in dataAlumnos:
           dicAlumno = {
                 'nombre': alumno.nombre,
                 'email': alumno.email
           } 
           lstAlumnos.append(dicAlumno)
      
      context = {
            'status':'Ok',
            'data':lstAlumnos
      }
           
      return JsonResponse(context)

@api_view(['GET'])
def getAlumnos(request):
      lstAlumnos = Alumno.objects.all()
      serAlumnos = AlumnoSerializer(lstAlumnos, many=True)
      context = {
            'status': 'Ok',
            'data': serAlumnos.data
      }
      return Response(context)
      
@api_view(['POST'])
def setAlumno(request):
      serAlumno = AlumnoSerializer(data=request.data)
      serAlumno.is_valid(raise_exception=True)
      
      nuevoAlumno = serAlumno.save()
      
      context = {
            'status': 'Ok',
            'message': 'Alumno creado',
            'data': AlumnoSerializer(nuevoAlumno).data
      }
      
      return Response(context)

####### ENDPOINT PROFESOR


@api_view(['GET', 'POST'])
def profesor(request):
      if request.method == 'GET':
            lstProfesores = Profesor.objects.all()
            serProfesores = ProfesorSerializer(lstProfesores, many=True)
            
            return Response(serProfesores.data)
      elif request.method == 'POST':
            serProfesor = ProfesorSerializer(data=request.data)
            if serProfesor.is_valid():
                  serProfesor.save()
                  return Response(serProfesor.data)
            else:
                  return Response(serProfesor.errors)
            
@api_view(['GET', 'PUT', 'DELETE'])
def profesor_detail(request, profesor_id):
      objProfesor=Profesor.objects.get(id=profesor_id)
      
      if request.method == "GET":
            serProfesor=ProfesorSerializer(objProfesor)
            return Response(serProfesor.data)
      
      elif request.method=='PUT':
            serProfesor=ProfesorSerializer(objProfesor,data=request.data)
            if serProfesor.is_valid():
                  serProfesor.save()
                  return Response (serProfesor.data)
            else:
                  return Response (serProfesor.errors)
      elif request.method=='DELETE':
            objProfesor.delete()
            return Response(status=204)
            
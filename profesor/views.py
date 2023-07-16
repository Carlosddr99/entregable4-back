from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Profesor
from .serializer import ProfesorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,permissions, authentication

# Create your views here.
@api_view(['GET'])
def obtenerAsignaturaProfesor(request,*args, **kwargs):
    
    if(request.data.get("id") != None):
        id = request.data.get("id")
    else:
        return Response("Error al buscar asignatura", status = 400)

    try:
        profesor = Profesor.objects.get(id=id)
    except:
        return Response("El profesor no existe", status = 404)

    return Response({"profesor": profesor.nombre, "asignatura":profesor.asignatura.nombre})      


class ProfesorViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Profesor.objects.all()
        serializer_class = ProfesorSerializer(queryset, many=True)
        return Response(serializer_class.data)

class ProfesorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    authentication_classes =[authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class ProfesorCreateAPIView(generics.ListCreateAPIView):  
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    authentication_classes =[authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class ProfesorUpdateAPIView(generics.UpdateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    authentication_classes =[authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


class ProfesorDestroyAPIView(generics.DestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    authentication_classes =[authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]






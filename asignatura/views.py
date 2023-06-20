from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Asignatura
from .serializer import AsignaturaSerializer

# Create your views here.

class AsignaturaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer


class AsignaturaCreateAPIView(generics.ListCreateAPIView):  
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class AsignaturaUpdateAPIView(generics.UpdateAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer


class AsignaturaDestroyAPIView(generics.DestroyAPIView):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer






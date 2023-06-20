
from .models import Profesor
from rest_framework import serializers;

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['nombre', 'edad', 'asignatura']
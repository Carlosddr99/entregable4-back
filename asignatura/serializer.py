
from .models import Asignatura
from rest_framework import serializers;

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'curso']
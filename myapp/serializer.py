# app/serializers.py

from rest_framework import serializers
from .models import usuario, Foro, Foro_Participacion, Informe_Proyecto

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = '__all__'

class Foro_ParticipacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro_Participacion
        fields = '__all__'

class Informe_ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe_Proyecto
        fields = '__all__'

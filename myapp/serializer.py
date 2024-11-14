# app/serializers.py

from rest_framework import serializers
from .models import usuario, Foro, Foro_Participacion, Informe_Proyecto
from django.utils import timezone

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario 
        fields = (
            'username',
            'password',
            'correo',
            'rol',
            'Fecha_Registro',
        )

    extra_kwargs = {
        'password': {'write_only': True}
    }

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        return value


    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario_instance = usuario(**validated_data)
        usuario_instance.set_password(password)
        usuario_instance.save()
        return usuario_instance
     
    def validate_fecha_registro(self, value):
        if value > timezone.now().date():    
            return value


class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = (
            'foro',
            'titulo',
            'descripcion',
            'Tema',
            'fechaCreacion',
        )

    def validate_fechaCreacion(self, value):
        if value > timezone.now().date(): 
            raise serializers.ValidationError("La fecha de creación no puede ser en el futuro.")
        return value

class Foro_ParticipacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro_Participacion
        fields = (
            'foro',
            'username',
            'FechaParticipacion',
        )
    
    def validate_fechaParticipacion(self, value):
        if value > timezone.now().date(): 
            raise serializers.ValidationError("La fecha de participación no puede ser en el futuro.")
        return value

class Informe_ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe_Proyecto
        fields = (
            'Id_reporte',
            'titulo',
            'descripcion',  
            'FechaSubida',
        )

    def validate_descripcion(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return value

    def validate_FechaSubida(self, value):
        if value > timezone.now().date(): 
            raise serializers.ValidationError("La fecha de subida no puede ser en el futuro.")
        return value

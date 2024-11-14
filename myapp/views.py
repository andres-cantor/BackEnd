from rest_framework import viewsets
from .models import usuario, Foro, Foro_Participacion, Informe_Proyecto
from .serializer import usuarioSerializer, ForoSerializer, Foro_ParticipacionSerializer, Informe_ProyectoSerializer

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

class ForoViewSet(viewsets.ModelViewSet):
    queryset = Foro.objects.all()
    serializer_class = ForoSerializer

class Foro_ParticipacionViewSet(viewsets.ModelViewSet):
    queryset = Foro_Participacion.objects.all()
    serializer_class = Foro_ParticipacionSerializer

class Informe_ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Informe_Proyecto.objects.all()
    serializer_class = Informe_ProyectoSerializer

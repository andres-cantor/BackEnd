# app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import usuarioViewSet, ForoViewSet, Foro_ParticipacionViewSet, Informe_ProyectoViewSet

# Crear el router y registrar las vistas
router = DefaultRouter()
router.register(r'usuario', usuarioViewSet, basename='usuario')
router.register(r'foros', ForoViewSet, basename='foros')
router.register(r'foro-participaciones', Foro_ParticipacionViewSet, basename='foro-participaciones')
router.register(r'informe-proyectos', Informe_ProyectoViewSet, basename='informe-proyectos')

# Incluir las rutas del router
urlpatterns = [
    path('', include(router.urls)),
]

# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),  # Asegúrate de cambiar 'app' por el nombre real de tu aplicación
]

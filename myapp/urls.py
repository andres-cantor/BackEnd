# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crea un router y registra tus viewsets
router = DefaultRouter()
router.register(r'usuarios', views.usuarioViewSet)
router.register(r'foros', views.ForoViewSet)
router.register(r'foro_participacion', views.Foro_ParticipacionViewSet)
router.register(r'informes', views.Informe_ProyectoViewSet)

urlpatterns = [
    path('', include(router.urls)),  

]
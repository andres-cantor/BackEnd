# BackDecisionesVerdes/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Incluye las rutas de la API aquí
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Genera el esquema de la API
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Accede a la documentación

    # Redirige la ruta raíz a la documentación (swagger-ui)
    path('', RedirectView.as_view(url='/docs/', permanent=False)),  # Redirige a /docs
]

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'api'

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
    path('auth/', include('api.auth.urls')),
    path('users/', include('users.urls')),
]

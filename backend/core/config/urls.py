from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from src.routes import routes

from .yasg import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(routes)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path(
        "swagger/",
        schema_view.with_ui("swagger"),
        name="schema-swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

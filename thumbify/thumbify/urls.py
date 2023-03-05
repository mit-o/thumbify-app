from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Thumbify API", default_version="1.0.0", description="API for Thumbify"
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/v1/",
        include(
            [
                path(
                    "",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="schema-swagger-ui",
                ),
                path("", include("apps.accounts.urls")),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

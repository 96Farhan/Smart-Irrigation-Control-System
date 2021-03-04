"""
Module Name: urls
Descriptipn: API URL's
"""
from django.urls import include, path
from rest_framework import routers
from iot import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Smart Irrigation Control System",
      default_version='v1',
      description="Smart Irrigation Control System REST API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


admin.site.site_header = "Smart Irrigation Control System Administration"
router = routers.DefaultRouter()
router.register(
    r'users',
    views.UserViewSet
)
router.register(
    r'groups',
    views.GroupViewSet
)
router.register(
    r'alerts',
    views.AlertViewSet
)

# Wire up your API using automatic URL routing.
urlpatterns = [
    path(
        r'api/', include(router.urls)),
    path(
        r'', admin.site.urls),
    path(
        r'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    path(
        r'redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='schema-redoc'
    ),
    path(
        r'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

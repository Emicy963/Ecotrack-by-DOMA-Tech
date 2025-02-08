from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="Sustainable Actions API",
        default_version='v1',
        description="API para registro de ações sustentáveis",
        contact=openapi.Contact(email="emicy963@duck.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.actions.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
] 

urlpatterns += staticfiles_urlpatterns()

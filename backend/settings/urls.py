"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#  from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static

urlpatterns = [
    path('api/core/', include('core.urls')),
    path('api/user/', include('user.urls')),
] 

if settings.DEBUG:
    from django.contrib import admin
    urlpatterns +=  path('admin/', admin.site.urls),

    schema_view = get_schema_view(
       openapi.Info(
          title="API Documentation",
          default_version='v1',
          description="API from django-vue Scaffold",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="contato@phsolucoesweb.com.br"),
          license=openapi.License(name="No License"),
       ),
       public=True, #if False, includes only endpoints the current user has access to
       permission_classes=(permissions.AllowAny,), 
    )
    #Swagger
    urlpatterns += [
       path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
       path('__debug__/', include('debug_toolbar.urls')),
    ]

if settings.DEBUG or settings.SERVE_MEDIA_LOCALLY:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

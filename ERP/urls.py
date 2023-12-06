"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
urlpatterns = [
        path('', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('api_schema', get_schema_view(title="VTS API Schema", description="VTS API Schema"), name='api_schema'),
    path('admin/', admin.site.urls),
    path('login', TokenObtainPairView.as_view(), name='Login '),
    path('user/',include('user.urls')),
    path('project/', include('projects.urls')),
    path('services/', include('services.urls')),
    path('meeting_schedule/', include('meeting_schedule.urls')),
]

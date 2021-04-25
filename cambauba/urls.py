"""cambauba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from core import urls as core_urls

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(template_name='login/index.html')),
    path('login/', auth_views.LoginView.as_view(template_name='login/index.html')),
    path('admin/', admin.site.urls),
    path('core/', include(core_urls)),
    path('', include('home.urls')),
    path('enquetes/', include('enquetes.urls')),
    path('atividades/', include('atividades.urls')),
    path('atividades_escolares/', include('atividades_escolares.urls')),
    path('informativos/', include('informativos.urls')),
    path('materiais_didaticos/', include('materiais_didaticos.urls')),
    path('turmas/', include('escolas.urls')),
    path('avatar/', include('avatar.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Gestor Cambauba"
admin.site.index_title = "Sistema de Administração"
admin.site.site_title = "Sistema de Gestão Cambauba"

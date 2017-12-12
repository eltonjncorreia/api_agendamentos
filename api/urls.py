from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter, SimpleRouter
from api.agendamentos import views
from api import agendamentos
from rest_framework_swagger.views import get_swagger_view



schema_view = get_swagger_view(title='API Agendamento')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('agendamentos', include('api.agendamentos.urls', namespace='agenda')),
    path('docs/', schema_view)

]
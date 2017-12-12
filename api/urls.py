from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter, SimpleRouter
from api.agendamentos import views
from api import agendamentos
from rest_framework_swagger.views import get_swagger_view

# router = DefaultRouter()
# # router.register('agendamentos', views.AgendamentosViewSet)
# # router.register('agendamentos/agendar', views.AgendamentosViewSet)
# # router.register('agendamentos/remarcar', views.AgendamentosViewSet)
# # router.register('agendamentos/cancelar', views.AgendamentosViewSet)
# # router.register('agendamentos/detalhes', views.AgendamentosViewSet)


schema_view = get_swagger_view(title='API Agendamento')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    # path('', include(router.urls)),
    path('agendamentos/', include('api.agendamentos.urls', namespace='agenda')),
    path('docs/', schema_view)

]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.agendamentos import views
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register('agendamentos/', views.AgendamentosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('agendamentos/', include('api.agendamentos.urls', namespace='agenda')),
    path('docs/', include_docs_urls(title='My API Agendamentos', public=False))

]
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view



schema_view = get_swagger_view(title='API Agendamento')


urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    path('', schema_view),
    re_path(r'agendamentos/', include('api.agendamentos.urls', namespace='agenda', )),
    re_path(r'docs/', schema_view)

]
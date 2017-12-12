from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from api.agendamentos import views


get_list = views.AgendamentosViewSet.as_view({
    'get': 'list',
})

post_create = views.AgendamentosViewSet.as_view({
    'post': 'create'
})


put_update_retrieve = views.AgendamentosViewSet.as_view({
    'put': 'update',
    'get': 'retrieve',
    'delete': 'destroy'
})


app_name = 'agenda'

urlpatterns = [
    path('', get_list, name='listagem'),
    path('agendar/', post_create, name='create'),
    path('remarcar/<int:pk>/', put_update_retrieve, name='atualizar'),
    path('cancelar/<int:pk>/', put_update_retrieve, name='deletar'),
    path('detalhes/<int:pk>/', put_update_retrieve, name='detalhes'),

]

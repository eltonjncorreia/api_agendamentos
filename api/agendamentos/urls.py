from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view

from api.agendamentos import views


get_list = views.AgendamentosViewSet.as_view({
    'get': 'list',

})

post_create = views.AgendamentosViewSet.as_view({
    'post': 'create'
})


put_update = views.AgendamentosViewSet.as_view({
    'put': 'update',

})


get_retrieve = views.AgendamentosViewSet.as_view({
    'get': 'retrieve',
})

detete_detroy =views.AgendamentosViewSet.as_view({
    'delete': 'destroy'
})

app_name = 'agenda'

urlpatterns = [
    path('', get_list, name='listagem'),
    re_path(r'agendar/', post_create, name='create'),
    re_path(r'remarcar/(?P<pk>\d+)/', put_update, name='atualizar'),
    re_path(r'cancelar/(?P<pk>\d+)/', detete_detroy, name='deletar'),
    re_path(r'detalhes/(?P<pk>\d+)/', get_retrieve, name='detalhes'),

]

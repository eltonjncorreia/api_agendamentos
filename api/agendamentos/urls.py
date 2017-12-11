from django.urls import path
from api.agendamentos import views

get_and_post = views.AgendamentosViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
put_delete_retrieve = views.AgendamentosViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

app_name = 'agenda'




urlpatterns = [
    path('', get_and_post, name='listagem'),
    path('agendar/', get_and_post, name='create'),
    path('remarcar/<int:pk>/', put_delete_retrieve, name='atualizar'),
    path('cancelar/<int:pk>/', put_delete_retrieve, name='deletar'),
    path('detalhe-agenda/<int:pk>/', put_delete_retrieve, name='detalhe'),
]

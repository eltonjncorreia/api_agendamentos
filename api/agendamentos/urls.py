from django.urls import path

from api.agendamentos import views

agendamento_lista = views.AgendamentosViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
agendamento_detail = views.AgendamentosViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

app_name = 'agenda'

urlpatterns = [
    path('', agendamento_lista, name='lista'),
    path('<int:pk>/', agendamento_detail, name='detail'),
]

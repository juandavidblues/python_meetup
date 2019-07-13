from django.contrib import admin
from django.urls import path,include
from python_meetup.mensajes.views import MensajeCreateView,MensajeListView,MensajeUpdateView,MensajeDeleteView
    

app_name = 'mensajes'

urlpatterns = [
    path('crear/', MensajeCreateView.as_view(), name='crear'),
    path('listar/', MensajeListView.as_view(), name='listar'),
    path('editar/<int:pk>', MensajeUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>', MensajeDeleteView.as_view(), name='eliminar')
]
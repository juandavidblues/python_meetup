from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from python_meetup.mensajes.models import Mensaje
from python_meetup.mensajes.forms import MensajeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class MensajeCreateView(CreateView):
    model = Mensaje
    form_class = MensajeForm
    success_url = reverse_lazy('mensajes:listar')

@method_decorator(login_required, name='dispatch')
class MensajeListView(ListView):
    model = Mensaje

@method_decorator(login_required, name='dispatch')
class MensajeUpdateView(UpdateView):
    model = Mensaje
    form_class = MensajeForm
    success_url = reverse_lazy('usuarios:index')

@method_decorator(login_required, name='dispatch')
class MensajeDeleteView(DeleteView):
    model = Mensaje
    success_url = reverse_lazy('usuarios:index')

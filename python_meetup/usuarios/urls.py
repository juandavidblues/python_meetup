from django.contrib import admin
from django.urls import path,include
from python_meetup.usuarios.views import LoginView,IndexView,LogoutView
    

app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='index')
]
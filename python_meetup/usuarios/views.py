from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from python_meetup.usuarios.forms import LoginForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'usuarios/index.html'

class LoginView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('usuarios:index')
        login_form = LoginForm()
        return render(request,'usuarios/login.html',{'form':login_form})
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('usuarios:index')
        else:
            return redirect('usuarios:login')

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('usuarios:login')
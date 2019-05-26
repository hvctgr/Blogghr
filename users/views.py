from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.views import View

from users.forms import LoginForm, SignupForm


class LoginView(View):

    def render_template_with_form(self, request, form):
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return self.render_template_with_form(request, form)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)
        return self.render_template_with_form(request, form)


class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('login')


class SignupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is None:
                messages.error(request, 'Usuario incorrecto')
            else:
                django_login(request, user)
                return redirect('home')

        context = {'form': form}
        return render(request, 'users/login.html', context)

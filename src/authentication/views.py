from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy('requests:list')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'login/register.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('requests:list')


def logout_user(request):
    logout(request)
    return redirect('authentication:login')


def redirection(request):
    if request.user.is_authenticated:
        return redirect('requests:list')
    return redirect('login/')

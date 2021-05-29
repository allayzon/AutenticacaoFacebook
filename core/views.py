from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin  # Faz com que o usuário deva estar logado em determinada view


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'

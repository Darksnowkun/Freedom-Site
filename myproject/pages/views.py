from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from accounts.models import MyUser
from django.utils import timezone

# Create your views here.

class Home(TemplateView):
    template_name = "index.html"

class About(DetailView):
    model = MyUser
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class Register(CreateView):
    model = MyUser
    template_name = "register.html"
    fields = '__all__'
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'about_content']
    success_url = "/"

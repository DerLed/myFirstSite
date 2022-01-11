from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import *
from .utils import DataMixin


# def index(request):
#     posts = Todo.objects.all()
#     return render(request, 'todo/index.html', {'posts': posts})


class TodoHome(DataMixin, ListView):
    model = Todo
    template_name = 'todo/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Главная страница'}

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return None
        return Todo.objects.filter(author=self.request.user)


class AddTask(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTask
    template_name = 'todo/addtask.html'
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Добавление задачи'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect('index')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'is_solved']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect('index')

    def has_permissions(self):
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class SignUp(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'todo/signup.html'
    success_url = reverse_lazy('index')
    extra_context = {'title': 'Регистрация'}


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'todo/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    """Функция выхода из учетной записи пользователя"""
    logout(request)
    return redirect('index')


class DeleteTask(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')

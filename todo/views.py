from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h1>ПРИВЕТ МИР!!!</h1>')

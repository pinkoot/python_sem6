from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tasks_osint(request):
    return HttpResponse("Задачи ОСИНТ")

# Create your views here.
def tasks_reverse(request):
    return HttpResponse("Задачи Реверс")


def tasks(request):
    return HttpResponse("Главная")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def catalog_info(request):

    template_name = 'catalog/catalog_detail.html'

    return render (request, template_name=template_name)

def main_page(request):
    return HttpResponse("Главная")

def catalog_detail(request, pk):
    return HttpResponse(f"Страница номер {pk} каталога")

def catalog_category(request, category):
    return HttpResponse(f"Страница категории {category}")


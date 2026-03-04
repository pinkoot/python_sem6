from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def catalog_info(request):

    template_name = 'catalog/catalog_detail.html'

    return render (request, template_name=template_name)

def main_page(request):
    return HttpResponse("Главная")

def catalog_detail(request, pk):
    return HttpResponse(f"Страница номер {pk} каталога")


def catalog_detail_test(request):

    template_name = 'catalog/catalog_detail.html'

    title = "test_title"
    promo_products = [
        'promo_product',
        'promo_product2',
        'promo_product3',
        'promo_product4',
    ]

    my_date = datetime.datetime(2026, 2, 28)

    context = {
        'title': title,
        'long_string': 'dfghjkldfghjkldfghj', 
        'html_test': '<h2> testtest </h2>',
        'promo_products': promo_products,
        'string_with_new_lines': 'aaa\nbbbb\nccc',
        'my_date': my_date,
        'test_text': 'ЭТО ОдиН МаЛЕНький шаг для челоВЕКА, Но БОЛьШой длЯ Еловечества'
    }

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )

def catalog_category(request, category):
    return HttpResponse(f"Страница категории {category}")
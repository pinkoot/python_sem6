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


def catalog_detail_test(request):

    template_name = 'catalog/catalog_detail.html'

    title = "test_title"
    promo_products = [
        'promo_product',
        'promo_product2',
        'promo_product3',
        'promo_product4',
    ]

    context = {
        'title': title,
        'promo_products': promo_products,
    }

    return render(
        request=request,
        template_name=template_name,
        context=context,
    )

def catalog_category(request, category):
    return HttpResponse(f"Страница категории {category}")
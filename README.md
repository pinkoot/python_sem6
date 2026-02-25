Быстрая разработка веб-приложений - DJANGO
1. Не повторяемся
2. Из коробки есть админка автоматом в любом созданном сайте
3. Из коробки ORM (Работа с базой данных как с объектами)
4. Не ассинхронный
5. Безопасность (защита от распространённых уязвимостей)
6. Шаблонизатор (jinja2)
7. Магазин расширений
python 3.12
python3.12 -m venv venv
pip install Django==3.2.16
Django-admin startproject bmstu_project .
Создание приложения: имя, структура файлов, генерируем
python manage.py startapp catalog
Необходимо:
8. Создать проект
Django-admin startproject bmstu_project .
9. Создать приложение
python manage.py startapp catalog
10. Зарегистрировать в проекте приложение (прописываем путь к классу приложения)
Пример структуры каталогов проекта:MyProject/
├── manage.py # утилита командной строки Django (запуск сервера, миграции,
создание приложений)
├── bmstu_project/
│ ├── __init__.py # пустой файл, делает папку пакетом Python
│ ├── asgi.py # точка входа для ASGI-серверов (асинхронный запуск)
│ ├── settings.py # настройки проекта (БД, приложения, статика, шаблоны)
│ ├── urls.py # главный файл маршрутизации (корневые URL-адреса)
│ └── wsgi.py # точка входа для WSGI-серверов (синхронный запуск)
├── catalog/
│ ├── migrations/
│ │ └── __init__.py # пакет для миграций БД
│ ├── __init__.py # пакет Python
│ ├── admin.py # настройка отображения моделей в админке
│ ├── apps.py # конфигурация приложения catalog
│ ├── models.py # модели данных (Product, Category и т.п.)
│ ├── tests.py # тесты приложения
│ ├── views.py # логика контроллеров (обработка запросов)
│ └── templates/
│
└── catalog/
│
├── product_list.html # шаблон списка товаров
│
└── product_detail.html # шаблон детальной страницы товара
├── basket/
│ ├── migrations/
│ │ └── __init__.py # пакет для миграций БД
│ ├── __init__.py # пакет Python
│ ├── admin.py # настройка отображения моделей в админке
│ ├── apps.py # конфигурация приложения basket
│ ├── models.py # модели данных (Cart, CartItem)
│ ├── tests.py # тесты приложения
│ ├── views.py # логика работы корзины
│ └── templates/
│
└── catalog/ # ОШИБКА: должно быть templates/basket/
│
├── product_list.html # (описка) шаблон страницы корзины
│
└── product_detail.html # (описка) шаблон элемента корзины
└── checkout/
├── __init__.py # пакет Python
├── models.py # модели данных (Order, OrderItem)
├── views.py # обработка оформления заказа
└── templates/
└── checkout/
└── order_confirmation.html # шаблон подтверждения заказа
Создаём ещё одно приложение:
11) Создать приложениеpython manage.py startapp basket
12. Зарегистрировать в проекте приложение (прописываем путь к классу приложения)
Планирование адресов и путей
# urls.py
from django.contrib import admin
from django.urls import path
from catalog import views
urlpatterns = [
path('/', views.main_page),
path('', views.main_page),
path('catalog/', views.catalog_info),
path('admin/', admin.site.urls),
]
# catalog.views.py
# from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def main_page(request):
return HttpResponse("Главная страница")
def catalog_info(request):
return HttpResponse("Страница каталога")Views функции пишем в соответствующих файла каждого приложения
ROOT_URLCONF = 'bmstu_project.urls'
самый главный файл urls
Запуск приложения:
python manage.py runserver
Конвертер путей (проброс пути в функцию)
<pk> - числа
обычная строка
слаг - латинские буквы , -
строка со слаг и инт
Задача к следующему разу(на субботу):
Проработать всё по уроку, начать писать свой сайт проекта
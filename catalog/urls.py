from django.urls import path

from . import views

urlpatterns = [
        path('', views.catalog_info),
        path('<int:pk>', views.catalog_detail),
        path('<slug:category>', views.catalog_category),


]

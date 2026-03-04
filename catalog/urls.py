from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
        path('', views.catalog_info, name='info'),
        path('<int:pk>', views.catalog_detail, name='detail' ),
        path('test/', views.catalog_detail_test, name ='test'),
        path('<slug:category>', views.catalog_category, name='category'),
]

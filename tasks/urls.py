from django.urls import path

from . import views

urlpatterns = [
        path('', views.tasks),
        path('reverse', views.tasks_reverse),
        path('osint', views.tasks_osint),


]

from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('Productos/', views.Productos, name='Productos'),
    path('Productos/ProductosDetalle/<', views.Plantilla, name='Plantilla'),
]
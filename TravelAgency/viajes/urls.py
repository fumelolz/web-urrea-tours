from django.urls import path
from . import views 

urlpatterns = [
    path('packages/', views.packageAll,name="core-packages"),
    path('destino/<int:destino_id>', views.destinoSingle,name="destino"),
    path('internacional/',views.packageInter,name="internacional"),
    path('nacional/',views.packageNacio,name="nacional"),
    path('search/',views.searchDestino,name="search"),
]
from django.urls import path
from .views import index, product_upgrete

urlpatterns = [
    path('', index, name='index'),
    path('productupgrete/', product_upgrete, name='product_upgrete'),
]
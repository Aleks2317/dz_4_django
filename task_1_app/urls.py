from django.urls import path
from .views import my_index, about


urlpatterns = [
    path('my_index/', my_index, name='my_index'),
    path('about/', about, name='about'),
]

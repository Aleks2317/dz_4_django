from django.urls import path
from .views import game, coin, cube, number, count_game_number, count_game_coin, count_game_cube

urlpatterns = [
    path('index/', game, name='game'),
    path('game_coin/', coin, name='coin'),
    path('game_cube/', cube, name='cube'),
    path('game_number/', number, name='number'),
    path('game_coin/<int:count>/', count_game_coin, name='count_game'),
    path('game_cube/<int:count>/', count_game_cube, name='count_game'),
    path('game_number/<int:count>/', count_game_number, name='count_game'),
]

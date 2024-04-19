import logging
from django.shortcuts import render
from random import randint, choice
from .models import Coin, Cube, Number
from .forms import Game_Form

logger = logging.getLogger(__name__)


def coin(request):
    resultat = []
    for _ in range(randint(1, 7)):
        result_random_game = choice(['Орел', 'Решка'])
        res_game = Coin(name='Орел или решка', result=result_random_game)
        res_game.save()
        resultat.append(result_random_game)

    context = {
        'resultat': enumerate(resultat, 1),
        'name_game': 'Орел или решка',
        'title': 'Game_coin'
    }
    return render(request, 'task_3_app/game.html', context)


def cube(request):
    resultat = []
    for _ in range(randint(1, 7)):
        result_random_game = randint(1, 7)
        res_game = Cube(name='Брось кубик', result=result_random_game)
        res_game.save()
        resultat.append(result_random_game)
    context = {
        'resultat': enumerate(resultat, 1),
        'name_game': 'Брось кубик',
        'title': 'Game_cobe'
    }
    return render(request, 'task_3_app/game.html', context)


def number(request):
    resultat = []
    for _ in range(1, 7):
        result_random_game = randint(1, 100)
        res_game = Number(name='Рандомное число от 1 до 100', result=result_random_game)
        res_game.save()
        resultat.append(result_random_game)
    context = {
        'resultat': enumerate(resultat, 1),
        'name_game': 'Рандомное число от 1 до 100',
        'title': 'Game_cobe'
    }
    return render(request, 'task_3_app/game.html', context)


def count_game_number(request, count: int = None):
    resultat = []
    for _ in range(count):
        result_random_game = randint(1, 100)
        res_game = Number(name='Рандомное число от 1 до 100', result=result_random_game)
        res_game.save()
        resultat.append(result_random_game)
    context = {
        'resultat': enumerate(resultat, 1),
        'name_game': 'Рандомное число от 1 до 100',
        'title': 'Game_number'
    }
    return render(request, 'task_3_app/game.html', context)


def count_game_coin(request, count: int = None):
    resultat = []
    for _ in range(count):
        result_random_game = choice(['Орел', 'Решка'])
        res_game = Coin(name='Орел или решка', result=result_random_game)
        res_game.save()
        resultat.append(result_random_game)
    context = {
        'resultat': enumerate(resultat, 1),
        'name_game': 'Орел или решка',
        'title': 'Game_coin'
    }
    return render(request, 'task_3_app/game.html', context)


def count_game_cube(request, count: int = None):
    resultat = []
    for _ in range(count):
        result_random_game = randint(1, 7)
        res_game = Cube(name='Брось кубик', result=result_random_game)
        res_game.save()
        resultat.append(result_random_game)
    context = {
        'resultat': enumerate(resultat, 1),
        'name_game': 'Брось кубик',
        'title': 'Game_cube'
    }
    return render(request, 'task_3_app/game.html', context)


def game(request):
    if request.method == 'POST':
        form = Game_Form(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count_game = form.cleaned_data['count_game']
            logger.info(f'Представление game {game = }, {count_game = }')
    else:
        form = Game_Form()
    return render(request, "task_3_app/index.html", {'form': form, 'title': 'Игра на выбор!'})

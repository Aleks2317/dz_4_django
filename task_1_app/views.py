from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def my_index(request):
    context = {
        "title": "Главная",
        "name": "Алексей"
    }
    logger.info(f"Посещена страница index.html")
    return render(request, "task_1_app/index.html", context)


def about(request):
    context = {
        "title": "About",
        "text": "Обо мне"
    }
    logger.info(f"Посещена страница about.html")
    return render(request, "task_1_app/about.html", context)



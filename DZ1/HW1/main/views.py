from django.shortcuts import render
from django.http import HttpResponse
import logging

# Создаем логгер
logger = logging.getLogger(__name__)

# Представление для главной страницы
def main(request):
    # HTML-вёрстка для главной страницы
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Мой первый Django сайт</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django сайт!</h1>
        <p>Здесь вы найдете информацию о моем проекте.</p>
    </body>
    </html>
    """
    # Записываем информацию о посещении страницы в лог
    logger.info('Пользователь посетил главную страницу')
    return HttpResponse(html)
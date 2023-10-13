from django.http import HttpResponse
import logging

# Создаем логгер
logger = logging.getLogger(__name__)

# Представление для страницы "О себе"
def about(request):
    # HTML-вёрстка для страницы "О себе"
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Всем зашедшим на данный сайт ПРИВЕТ! Я - Алексей. 
        Системный администратор и разработчик данного сайта приветствую Вас!</p>
        <h3>Связь со мной</h3>
        <p>Вы можете связаться со мной по электронной почте: alex05524@gmail.com.</p>
    </body>
    </html>
    """
    # Записываем информацию о посещении страницы в лог
    logger.info('Пользователь посетил страницу "О себе"')
    return HttpResponse(html)
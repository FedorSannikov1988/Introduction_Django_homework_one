import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):

    ip_user = request.META.get('REMOTE_ADDR',
                               'Не удалось получить IP-адрес пользователя')
    logger.info(f'ip address user: {ip_user}, page: index')

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на "Главную страницу".</h1>
        <p>Здесь вы найдете информацию о моем проекте на Django.</p>
        <h2>О проекте:</h2>
        <p>Мой проект на Django это одно простое веб-приложение.</p>
        <p>Оно содержит несколько страниц (index - Главная станица и about_me - Обо мне).</p>
    </body>
    </html>
    """

    return HttpResponse(html)


def about_me(request):

    ip_user = request.META.get('REMOTE_ADDR',
                               'Не удалось получить IP-адрес пользователя')
    logger.info(f'ip address user: {ip_user}, page: about_me')

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Обо мне</title>
    </head>
    <body>
        <h1>Добро пожаловать в раздел "Обо мне"</h1>
        <p>Меня зовут Федор.</p>
        <p>Я начинающий разработчик и этот проект - моя первая домашняя работа по Django.</p>
        <p>Я увлекаюсь программированием и хочу развиваться в этой области.</p>
    </body>
    </html>
    """

    return HttpResponse(html)
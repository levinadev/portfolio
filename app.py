from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Foodgram",
        "image": "Foodgram.png",
        "img_alt": "Foodgram",
        "description": (
            "Сервис для публикации рецептов с аккаунтами пользователей, избранным, "
            "подписками, списками покупок и управлением рецептами."
        ),
        "github": "https://github.com/levinadev/foodgram",
        "demo": "https://foodgram.levinadev.ru/",
    },
    {
        "title": "YaCut",
        "image": "async-yacut.png",
        "img_alt": "YaCut",
        "description": (
            "Сервис сокращения ссылок для создания коротких URL и публикации "
            "пользовательских ссылок на скачивание файлов."
        ),
        "github": "https://github.com/levinadev/async-yacut",
        "demo": "https://yacut.levinadev.ru/",
    },
    {
        "title": "QRkot",
        "image": "QRkot_spreadsheets.png",
        "img_alt": "QRkot",
        "description": (
            "API для благотворительного сервиса помощи кошкам: аутентификация, "
            "пожертвования, проекты, роли и отчеты в Google Sheets."
        ),
        "github": "https://github.com/levinadev/QRkot_spreadsheets",
        "demo": "https://qrkot.levinadev.ru/docs",
    },
    {
        "title": "Scrapy-парсер PEP",
        "image": "scrapy_parser_pep.png",
        "img_alt": "Scrapy-парсер PEP",
        "description": (
            "Асинхронный парсер на Scrapy для сбора данных PEP и выгрузки отчетов в CSV."
        ),
        "github": "https://github.com/levinadev/scrapy_parser_pep",
        "demo": None,
    },
    {
        "title": "Бронирование переговорных",
        "image": "room_reservation_spreadsheets.png",
        "img_alt": "Бронирование переговорных",
        "description": (
            "Приложение на FastAPI для бронирования переговорных с интеграциями "
            "Google API и таблиц."
        ),
        "github": "https://github.com/levinadev/room_reservation_spreadsheets",
        "demo": "https://room.levinadev.ru/docs",
    },
    {
        "title": "Kittygram",
        "image": "kittygram_final.png",
        "img_alt": "Kittygram",
        "description": (
            "Приложение для публикации фото питомцев на Django, DRF, React, "
            "PostgreSQL, Docker и Nginx."
        ),
        "github": "https://github.com/levinadev/kittygram_final",
        "demo": "https://kittygram.levinadev.ru/",
    },
]


@app.get("/")
def index():
    return render_template("index.html", projects=PROJECTS)


@app.get("/about")
def about():
    return render_template("about.html")

from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Foodgram",
        "image": "Foodgram.png",
        "description": (
            "Recipe sharing service with user accounts, favorites, subscriptions, "
            "shopping lists, and recipe management."
        ),
        "github": "https://github.com/levinadev/foodgram",
        "demo": "https://foodgram.levinadev.ru/",
    },
    {
        "title": "YaCut",
        "image": "async-yacut.png",
        "img_alt": "YaCut",
        "description": (
            "Link shortener service for creating short URLs and sharing custom "
            "file download links online."
        ),
        "github": "https://github.com/levinadev/async-yacut",
        "demo": "https://yacut.levinadev.ru/",
    },
    {
        "title": "QRkot",
        "image": "QRkot_spreadsheets.png",
        "img_alt": "QRkot_spreadsheets",
        "description": (
            "Cat charity API with authentication, donations, projects, roles, "
            "and Google Sheets reports."
        ),
        "github": "https://github.com/levinadev/QRkot_spreadsheets",
        "demo": "https://qrkot.levinadev.ru/docs",
    },
    {
        "title": "Scrapy Parser PEP",
        "image": "scrapy_parser_pep.png",
        "img_alt": "scrapy_parser_pep",
        "description": (
            "Scrapy-based async parser for collecting PEP data and exporting CSV reports."
        ),
        "github": "https://github.com/levinadev/scrapy_parser_pep",
        "demo": None,
    },
    {
        "title": "Room Reservation",
        "image": "room_reservation_spreadsheets.png",
        "img_alt": "room_reservation_spreadsheets",
        "description": (
            "FastAPI app for meeting room booking with Google API and spreadsheet integrations."
        ),
        "github": "https://github.com/levinadev/room_reservation_spreadsheets",
        "demo": "https://room.levinadev.ru/docs",
    },
    {
        "title": "Kittygram",
        "image": "kittygram_final.png",
        "img_alt": "kittygram_final",
        "description": (
            "A pet photo sharing app with Django, DRF, React, PostgreSQL, Docker, and Nginx."
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

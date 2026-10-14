import datetime

from flask import Flask, abort, render_template

FAVORITES = [
    {"id": 1, "title": "Honkai Star Rail", "why": "The animations are pretty and I enjoy turn-based combat"},
    {"id": 2, "title": "Minions", "why": "They are cute"},
    {"id": 3, "title": "Reading", "why": "I like reading about fictional worlds"},
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

def index():
    return render_template("index.html",
                           name="Maya",
                           hobby="Playing video games",
                           hours_per_week=14,
                           hour=datetime.now().hour,
                           show_counter=False,
                           favorites=FAVORITES)

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)

def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
from datetime import datetime

from flask import Flask, abort, render_template

FAVORITES = [
    {"id": 1, "title": "Honkai Star Rail", "why": "The animations are pretty and I enjoy turn-based combat"},
    {"id": 2, "title": "Minions", "why": "They are cute"},
    {"id": 3, "title": "Reading", "why": "I like reading about fictional worlds"},
]

GAMES = [
    {"title": "Honkai Star Rail", "genre": "Turn-based RPG", "hours": 100, "rating": 7.5,
     "status": "Playing", "notes": "Daily tasks, story content"},
    {"title": "Genshin Impact", "genre": "Open-world RPG", "hours": 50, "rating": 7,
     "status": "Playing", "notes": "It really needs a skip button"},
    {"title": "Baldur's Gate 3", "genre": "RPG", "hours": 808, "rating": 9,
     "status": "Completed", "notes": "Almost everything about the game is amazing"},
    {"title": "Persona 5", "genre": "Turn-based RPG", "hours": 188, "rating": 8.5,
     "status": "Completed", "notes": "Great soundtrack and gameplay, good story"},
    {"title": "Cyberpunk 2077", "genre": "Open-world RPG", "hours": 4, "rating": None,
     "status": "Backlog", "notes": "It is the type of game I would love but I replay games too much"},
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

def index():
    return render_template("index.html",
                           name="Maya",
                           hobby="playing video games",
                           hours_per_week=14,
                           hour=datetime.now().hour,
                           show_counter=False,
                           favorites=FAVORITES)

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)

def games():
    return render_template("games.html", games=GAMES, goal_hours=500)

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/games")(games)

def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
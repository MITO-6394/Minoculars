from flask import Flask
from routes import *


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=9999, debug=True)



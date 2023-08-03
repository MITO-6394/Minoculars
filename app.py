from flask import Flask


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"


from routes import *


if __name__ == "__main__":
    app.run(port=9999, debug=True)

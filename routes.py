from app import app
from db import *
from flask import render_template, jsonify, request


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    form = request.form
    db.session.add(PlaysIn(
        team_num=form.get("team_num"),
        game_id=form.get("game_id"),
        auto_shoots=form.get("auto_shoots"),
        auto_goals=form.get("auto_goals"),
        teleop_shoots=form.get("teleop_shoots"),
        teleop_goals=form.get("teleop_goals"),
        climb_score=form.get("climb_score"),
        foul=form.get("foul")
    ))
    db.session.commit()
    return render_template("success.html")
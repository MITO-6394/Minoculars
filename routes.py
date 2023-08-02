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
        taxi_tarmac=True if form.get("taxi_tarmac") == "on" else False,
        auto_upper=form.get("auto_upper"),
        auto_upper_fail=form.get("auto_upper_fail"),
        auto_lower=form.get("auto_lower"),
        teleop_upper=form.get("teleop_upper"),
        teleop_upper_fail=form.get("teleop_upper_fail"),
        teleop_lower=form.get("teleop_lower"),
        climb_rung=form.get("climb_rung"),
        climb_fail=True if form.get("climb_fail") == "on" else False,
        climb_pos=form.get("climb_pos"),
        foul=form.get("foul"),
        comments=form.get("comments")
    ))
    db.session.commit()
    return render_template("success.html")

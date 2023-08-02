from sqlalchemy.orm import backref

from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Team(db.Model):
    num = db.Column(db.Integer, primary_key=True)

    # games = db.relationship("Game", secondary="plays_in")


class Game(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    blue_1 = db.Column(db.Integer, db.ForeignKey("plays_in.team_num"))
    blue_2 = db.Column(db.Integer, db.ForeignKey("plays_in.team_num"))
    blue_3 = db.Column(db.Integer, db.ForeignKey("plays_in.team_num"))
    red_1 = db.Column(db.Integer, db.ForeignKey("plays_in.team_num"))
    red_2 = db.Column(db.Integer, db.ForeignKey("plays_in.team_num"))
    red_3 = db.Column(db.Integer, db.ForeignKey("plays_in.team_num"))

    # teams = db.relationship("Team", secondary="plays_in")


class PlaysIn(db.Model):
    team_num = db.Column(db.Integer, db.ForeignKey("team.num"), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), primary_key=True)
    taxi_tarmac = db.Column(db.Boolean)
    auto_upper = db.Column(db.Integer)
    auto_upper_fail = db.Column(db.Integer)
    auto_lower = db.Column(db.Integer)
    teleop_upper = db.Column(db.Integer)
    teleop_upper_fail = db.Column(db.Integer)
    teleop_lower = db.Column(db.Integer)
    climb_rung = db.Column(db.String(9))
    climb_fail = db.Column(db.Boolean)
    climb_pos = db.Column(db.String(6))
    foul = db.Column(db.Integer)
    comments = db.Column(db.Text)

    # team = db.relationship(Team, backref=backref("plays_in"))
    # game = db.relationship(Game, backref=backref("plays_in"))


with app.app_context():
    db.create_all()

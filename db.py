from sqlalchemy.orm import backref

from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
    auto_shoots = db.Column(db.Integer)
    auto_goals = db.Column(db.Integer)
    teleop_shoots = db.Column(db.Integer)
    teleop_goals = db.Column(db.Integer)
    climb_score = db.Column(db.Integer)
    foul = db.Column(db.Integer)

    # team = db.relationship(Team, backref=backref("plays_in"))
    # game = db.relationship(Game, backref=backref("plays_in"))


with app.app_context():
    db.create_all()

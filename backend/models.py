from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opponent = db.Column(db.String(50), nullable=False)
    minutes = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    rebounds = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    
    def to_json(self):
        return {
            "id": self.id,
            "opponent": self.opponent,
            "minutes": self.minutes,
            "points": self.points,
            "rebounds": self.rebounds,
            "assists": self.assists,
            "notes": self.notes
        }
    
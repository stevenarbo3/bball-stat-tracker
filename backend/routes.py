from app import app, db
from flask import request, jsonify
from models import Game

# get all games
@app.route('/api/games', methods=["GET"])
def get_games():
    games = Game.query.all()
    result = [game.to_json() for game in games]
    return jsonify(result)

# create a game
@app.route('/api/games', methods=['POST'])
def create_game():
    try:
        data = request.json
        
        opponent = data.get("opponent")
        minutes = data.get("minutes")
        points = data.get("points")
        rebounds = data.get("rebounds")
        assists = data.get("assists")
        notes = data.get("notes")
        
        new_game = Game(
            opponent=opponent,
            minutes=minutes,
            points=points,
            rebounds=rebounds,
            assists=assists,
            notes=notes)
        
        db.session.add(new_game)
        
        db.session.commit()
        
        return jsonify({"msg": "Game created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

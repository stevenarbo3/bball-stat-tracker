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
        
        required_fields = ["opponent", "minutes", "points", "rebounds", "assists", "notes"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error":f'Missing required field: {field}'}), 400
        
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
    
# delete a game
@app.route("/api/games/<int:id>", methods=['DELETE'])
def delete_game(id):
    try:
        game = Game.query.get(id)
        if game is None:
            return jsonify({"error": "game not found"}), 404
        
        db.session.delete(game)
        db.session.commit()
        
        return jsonify({"msg":"game deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500

# update a game
@app.route('/api/games/<int:id>', methods=['PATCH'])
def update_game(id):
    try:
        game = Game.query.get(id)
        if game is None:
            return jsonify({"error": "game not found"}), 404
        
        data = request.json
        
        game.opponent = data.get("opponent", game.opponent)
        game.minutes = data.get("minutes", game.minutes)
        game.points = data.get("points", game.points)
        game.rebounds = data.get("rebounds", game.rebounds)
        game.assists = data.get("assists", game.assists)
        game.notes = data.get("notes", game.notes)
        
        db.session.commit()
        return jsonify({"msg":"game updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
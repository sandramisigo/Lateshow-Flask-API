from flask import Flask, request, jsonify
from models import db, Episode, Guest, Appearance

app = Flask(__name__)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    else:
        return jsonify({'error': 'Episode not found'}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    if None in (rating, episode_id, guest_id):
        return jsonify({"errors": ["Missing required fields"]}), 400

    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({"errors": ["Episode or Guest not found"]}), 404

    try:
        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
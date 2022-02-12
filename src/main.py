"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Character, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#ADD USER
@app.route('/user/register', methods=['POST'])
def create_user():
    body=request.get_json()
    new_user=User(email=body['email'],password=body['password'],name=body['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 200

#GET 1 USER
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user=User.query.get(user_id)
    return jsonify(user.serialize()), 200

#GET ALL USERS
@app.route('/users',methods=['GET'])
def get_users():
    user_list=[]
    users=User.query.all()
    for user in users:
        user_list.append(user.serialize())
    return jsonify(user_list),200

#DELETE USER
@app.route('/users/<user_id>',methods=['DELETE'])
def delete_user(user_id):
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return jsonify("Borrado realizado"),200

#ADD PLANET
@app.route('/planets/add', methods=['POST'])
def create_planet():
    body=request.get_json()
    new_planet=Planet(name=body['name'])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(new_planet.serialize()), 200
#GET 1 PLANET
@app.route('/planets/<planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet=Planet.query.get(planet_id)
    return jsonify(planet.serialize()), 200
#GET ALL PLANETS
@app.route('/planets',methods=['GET'])
def get_planets():
    planet_list=[]
    planets=Planet.query.all()
    for planet in planets:
        planet_list.append(planet.serialize())
    return jsonify(planet_list),200

#DELETE PLANET
@app.route('/planets/<planet_id>',methods=['DELETE'])
def delete_planet(planet_id):
    Planet.query.filter(Planet.id == planet_id).delete()
    db.session.commit()
    return jsonify("Borrado realizado"),200


#ADD CHARACTER
@app.route('/characters/add', methods=['POST'])
def create_character():
    body=request.get_json()
    new_character=Character(name=body['name'],planet_id=body['planet_id'])
    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.serialize()), 200

#GET 1 CHARACTER
@app.route('/characters/<character_id>', methods=['GET'])
def get_character(character_id):
    character=Character.query.get(character_id)
    return jsonify(character.serialize()), 200

#GET ALL CHARACTERS
@app.route('/characters',methods=['GET'])
def get_characters():
    character_list=[]
    characters=Character.query.all()
    for character in characters:
        character_list.append(character.serialize())
    return jsonify(character_list),200

#DELETE CHARACTER
@app.route('/characters/<character_id>',methods=['DELETE'])
def delete_character(character_id):
    Character.query.filter(Character.id == character_id).delete()
    db.session.commit()
    return jsonify("Borrado realizado"),200


#ADD FAVORITE PLANET TO USER
@app.route('/<user_id>/favorites/planets/<planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    body=request.get_json()
    new_favorite_planet=Favorite(planet_id=planet_id, user_id=body['user_id'])
    db.session.add(new_favorite_planet)
    db.session.commit()
    return jsonify(new_favorite_planet.serialize()), 200

#ADD FAVORITE CHARACTER TO USER
@app.route('/<user_id>/favorites/characters/<character_id>', methods=['POST'])
def add_favorite_character(character_id):
    body=request.get_json()
    new_favorite_character=Favorite(character_id=character_id, user_id=body['user_id'])
    db.session.add(new_favorite_character)
    db.session.commit()
    return jsonify(new_favorite_character.serialize()), 200

#GET USER FAVORITES
@app.route('/<user_id>/favorites',methods=['GET'])
def get_user_favorites(user_id):
    favorites_list=[]
    favorites=Favorite.query.filter(Favorite.user_id==user_id)
    for favorite in favorites:
        favorites_list.append(favorite.serialize())
    return jsonify(favorites_list),200

#DELETE FAVORITE PLANET FROM USER
@app.route('/<user_id>/favorites/planets/<planet_id>',methods=['DELETE'])
def delete_favorite_planet(user_id,planet_id):
    Favorite.query.filter(Favorite.planet_id == planet_id).delete()
    db.session.commit()
    return jsonify("Borrado realizado"),200

#DELETE FAVORITE CHARACTER FROM USER
@app.route('/<user_id>/favorites/characters/<character_id>',methods=['DELETE'])
def delete_favorite_character(user_id,character_id):
    Favorite.query.filter(Favorite.character_id == character_id).delete()
    db.session.commit()
    return jsonify("Borrado realizado"),200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

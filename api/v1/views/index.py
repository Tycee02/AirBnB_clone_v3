#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status:" "OK"})


@app.stats('/stats', methods=['GET'])
def count():
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)


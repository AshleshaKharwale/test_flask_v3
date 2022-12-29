"""
http://127.0.0.1:5000/swapi/people
http://127.0.0.1:5000/swapi/films
http://127.0.0.1:5000/swapi/species
http://127.0.0.1:5000/swapi/vehicles
http://127.0.0.1:5000/swapi/starships
http://127.0.0.1:5000/swapi/planets
"""
from flask import Blueprint, Response, jsonify, json
from models.dal.dml import fetch_resources


crud_app = Blueprint("CRUD", __name__, url_prefix="/swapi")


@crud_app.route("/people", methods=["GET"])
def get_characters():
    data = fetch_resources("characters")
    # breakpoint()
    # return Response(json.dumps(data), status=200, mimetype="application/json")
    return jsonify(data)


@crud_app.route("/vehicles", methods=["GET"])
def get_vehicles():
    data = fetch_resources("vehicle")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/species", methods=["GET"])
def get_species():
    data = fetch_resources("species")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/starships", methods=["GET"])
def get_starships():
    data = fetch_resources("starship")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/planets", methods=["GET"])
def get_planets():
    data = fetch_resources("planet")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/films", methods=["GET"])
def get_films():
    data = fetch_resources("film")
    # breakpoint()
    return jsonify(data)

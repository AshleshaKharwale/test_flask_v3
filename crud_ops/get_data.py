"""
http://127.0.0.1:5000/swapi/people
http://127.0.0.1:5000/swapi/films (plural API endpoint)
http://127.0.0.1:5000/swapi/films/1 (singular API endpoint)
http://127.0.0.1:5000/swapi/species
http://127.0.0.1:5000/swapi/vehicles
http://127.0.0.1:5000/swapi/starships
http://127.0.0.1:5000/swapi/planets
"""
from flask import Blueprint, Response, jsonify, json
from models.dal.dml import fetch_resources, fetch_resource
from models.datamodels.characters import ResponseCharacters
from models.datamodels.films import ResponseFilms
from models.datamodels.vehicles import ResponseVehicles
from models.datamodels.species import ResponseSpecies
from models.datamodels.planets import ResponsePlanets
from models.datamodels.starships import ResponseStarships


crud_app = Blueprint("CRUD", __name__, url_prefix="/swapi")


@crud_app.route("/people", methods=["GET"])
def get_characters():
    data = fetch_resources("characters")
    # breakpoint()
    # return Response(json.dumps(data), status=200, mimetype="application/json")
    return jsonify(data)


@crud_app.route("/people/<int:index>")
def get_char(index):
    data = fetch_resource("characters", "char_id", index)
    # breakpoint()
    if data:
        data = ResponseCharacters(**data)
        return jsonify(data.dict())
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@crud_app.route("/vehicles", methods=["GET"])
def get_vehicles():
    data = fetch_resources("vehicle")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/vehicles/<int:index>")
def get_vehicle(index):
    data = fetch_resource("vehicle", "vehicle_id", index)
    # breakpoint()
    if data:
        data = ResponseVehicles(**data)
        return jsonify(data.dict())
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@crud_app.route("/species", methods=["GET"])
def get_species():
    data = fetch_resources("species")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/species/<int:index>")
def get_specie(index):
    data = fetch_resource("species", "species_id", index)
    # breakpoint()
    if data:
        data = ResponseSpecies(**data)
        return jsonify(data.dict())
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@crud_app.route("/starships", methods=["GET"])
def get_starships():
    data = fetch_resources("starship")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/starships/<int:index>")
def get_starship(index):
    data = fetch_resource("starship", "starship_id", index)
    # breakpoint()
    if data:
        data = ResponseStarships(**data)
        return jsonify(data.dict())
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@crud_app.route("/planets", methods=["GET"])
def get_planets():
    data = fetch_resources("planet")
    # breakpoint()
    return Response(json.dumps(data), status=200, mimetype="application/json")


@crud_app.route("/planets/<int:index>")
def get_planet(index):
    data = fetch_resource("planet", "planet_id", index)
    # breakpoint()
    if data:
        data = ResponsePlanets(**data)
        return jsonify(data.dict())
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@crud_app.route("/films", methods=["GET"])
def get_films():
    data = fetch_resources("film")
    # breakpoint()
    return jsonify(data)


@crud_app.route("/films/<int:index>")
def get_film(index):
    data = fetch_resource("film", "film_id", index)
    # breakpoint()
    if data:
        data = ResponseFilms(**data)
        return jsonify(data.dict())
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")

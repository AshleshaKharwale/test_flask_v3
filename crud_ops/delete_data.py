from flask import Blueprint, request, Response, json
from models.dal.dml import delete_resource


delete_data = Blueprint("delete_data", __name__, url_prefix="/swapi")


@delete_data.delete("/people/<int:id_>")
@delete_data.delete("/people")
def delete_character(id_=None):
    char_id = None
    if id_ is not None:
        char_id = id_
    else:
        # breakpoint()
        request_data = dict(request.args) if request.args else request.json
        char_id = request_data.get("char_id")

    result = delete_resource("characters", "char_id", char_id)
    response_obj = {
        "message": "Successfully deleted record!" if result else "No record available to delete.",
        "deleted_count": result,
        "char_id": char_id
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@delete_data.delete("/vehicles/<int:id_>")
@delete_data.delete("/vehicles")
def delete_vehicle(id_=None):
    vehicle_id = None
    if id_ is not None:
        vehicle_id = id_
    else:
        # breakpoint()
        request_data = dict(request.args) if request.args else request.json
        char_id = request_data.get("vehicle_id")

    result = delete_resource("vehicle", "vehicle_id", vehicle_id)
    response_obj = {
        "message": "Successfully deleted record!" if result else "No record available to delete.",
        "deleted_count": result,
        "vehicle_id": vehicle_id
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@delete_data.delete("/planets/<int:id_>")
@delete_data.delete("/planets")
def delete_planet(id_=None):
    planet_id = None
    if id_ is not None:
        planet_id = id_
    else:
        # breakpoint()
        request_data = dict(request.args) if request.args else request.json
        planet_id = request_data.get("planet_id")

    result = delete_resource("planet", "planet_id", planet_id)
    response_obj = {
        "message": "Successfully deleted record!" if result else "No record available to delete.",
        "deleted_count": result,
        "planet_id": planet_id
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@delete_data.delete("/species/<int:id_>")
@delete_data.delete("/species")
def delete_species(id_=None):
    species_id = None
    if id_ is not None:
        species_id = id_
    else:
        # breakpoint()
        request_data = dict(request.args) if request.args else request.json
        species_id = request_data.get("species_id")

    result = delete_resource("species", "species_id", species_id)
    response_obj = {
        "message": "Successfully deleted record!" if result else "No record available to delete.",
        "deleted_count": result,
        "species_id": species_id
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@delete_data.delete("/starships/<int:id_>")
@delete_data.delete("/starships")
def delete_starship(id_=None):
    starship_id = None
    if id_ is not None:
        starship_id = id_
    else:
        # breakpoint()
        request_data = dict(request.args) if request.args else request.json
        starship_id = request_data.get("starship_id")

    result = delete_resource("starship", "starship_id", starship_id)
    response_obj = {
        "message": "Successfully deleted record!" if result else "No record available to delete.",
        "deleted_count": result,
        "starship_id": starship_id
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@delete_data.delete("/films/<int:id_>")
@delete_data.delete("/films")
def delete_film(id_=None):
    film_id = None
    if id_ is not None:
        film_id = id_
    else:
        # breakpoint()
        request_data = dict(request.args) if request.args else request.json
        film_id = request_data.get("film_id")

    result = delete_resource("film", "film_id", film_id)
    response_obj = {
        "message": "Successfully deleted record!" if result else "No record available to delete.",
        "deleted_count": result,
        "film_id": film_id
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")

from flask import Blueprint, request, Response, json
from typing import Dict
from models.datamodels.characters import Characters
from models.datamodels.films import Films
from models.datamodels.planets import Planets
from models.datamodels.vehicles import Vehicles
from models.datamodels.starships import Starships
from models.datamodels.species import Species
from models.dal.dml import update_resource
from pydantic import ValidationError


put_data = Blueprint("put_data", __name__, url_prefix="/swapi")


def remove_cross_reference(data_set: "pydantic datamodel object") -> Dict:
    """
    1. Takes pydantic datamodel object as argument of any resource.
    2. Converts it to dictionary data type.
    3. Removes cross-reference fields if any. (ex., character["url1","url2"]) or None fields.
    4. Returns this formatted dictionary.

    :param data_set: validated pydantic data model object
    :return: Data in dictionary without cross-reference and None fields.
    """
    data_set = dict(data_set)
    new_data = data_set.copy()
    for key, value in data_set.items():
        if isinstance(value, list) or value is None:
            # removing cross-reference and None fields from data object
            new_data.pop(key)

    return new_data


@put_data.put("/people/<int:id_>")
@put_data.put("/people")
def put_character(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("char_id") is None:
        if id_ is not None:
            request_data["char_id"] = id_
        else:
            url = request_data.get("url")
            url = url.split("/")
            request_data["char_id"] = url[-2]

    response_obj = {}
    try:
        request_data = Characters(**request_data)
        request_data = remove_cross_reference(request_data)
        char_id = request_data.pop("char_id")
        result = update_resource("characters", request_data, "char_id", char_id)
        response_obj = {
            "rows_affected": result,
            "char_id": char_id,
            "message": "record updated successfully." if result else "Error! id doesn't exist."
        }

    except ValidationError as e:
        error_msg = str(e)
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@put_data.put("/vehicle/<int:id_>")
@put_data.put("/vehicle")
def put_vehicle(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("vehicle_id") is None:
        if id_ is not None:
            request_data["vehicle_id"] = id_
        else:
            url = request_data.get("url")
            url = url.split("/")
            request_data["vehicle_id"] = url[-2]

    response_obj = {}
    try:
        request_data = Vehicles(**request_data)
        request_data = remove_cross_reference(request_data)
        vehicle_id = request_data.pop("vehicle_id")
        result = update_resource("vehicle", request_data, "vehicle_id", vehicle_id)
        response_obj = {
            "rows_affected": result,
            "vehicle_id": vehicle_id,
            "message": "record updated successfully." if result else "Error! id doesn't exist."
        }

    except ValidationError as e:
        error_msg = str(e)
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@put_data.put("/film/<int:id_>")
@put_data.put("/film")
def put_film(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("film_id") is None:
        if id_ is not None:
            request_data["film_id"] = id_
        else:
            url = request_data.get("url")
            url = url.split("/")
            request_data["film_id"] = url[-2]

    response_obj = {}
    try:
        request_data = Films(**request_data)
        request_data = remove_cross_reference(request_data)
        film_id = request_data.pop("film_id")
        result = update_resource("film", request_data, "film_id", film_id)
        response_obj = {
            "rows_affected": result,
            "film_id": film_id,
            "message": "record updated successfully." if result else "Error! id doesn't exist."
        }

    except ValidationError as e:
        error_msg = str(e)
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@put_data.put("/species/<int:id_>")
@put_data.put("/species")
def put_species(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        if id_ is not None:
            request_data["species_id"] = id_
        else:
            url = request_data.get("url")
            url = url.split("/")
            request_data["species_id"] = url[-2]

    response_obj = {}
    try:
        request_data = Species(**request_data)
        request_data = remove_cross_reference(request_data)
        species_id = request_data.pop("species_id")
        result = update_resource("species", request_data, "species_id", species_id)
        response_obj = {
            "rows_affected": result,
            "species_id": species_id,
            "message": "record updated successfully." if result else "Error! id doesn't exist."
        }

    except ValidationError as e:
        error_msg = str(e)
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@put_data.put("/starships/<int:id_>")
@put_data.put("/starships")
def put_starship(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("starship_id") is None:
        if id_ is not None:
            request_data["starship_id"] = id_
        else:
            url = request_data.get("url")
            url = url.split("/")
            request_data["starship_id"] = url[-2]

    response_obj = {}
    try:
        request_data = Starships(**request_data)
        request_data = remove_cross_reference(request_data)
        starship_id = request_data.pop("starship_id")
        result = update_resource("starship", request_data, "starship_id", starship_id)
        response_obj = {
            "rows_affected": result,
            "starship_id": starship_id,
            "message": "record updated successfully." if result else "Error! id doesn't exist."
        }

    except ValidationError as e:
        error_msg = str(e)
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@put_data.put("/planets/<int:id_>")
@put_data.put("/planets")
def put_planet(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("planet_id") is None:
        if id_ is not None:
            request_data["planet_id"] = id_
        else:
            url = request_data.get("url")
            url = url.split("/")
            request_data["planet_id"] = url[-2]

    response_obj = {}
    try:
        request_data = Planets(**request_data)
        request_data = remove_cross_reference(request_data)
        planet_id = request_data.pop("planet_id")
        result = update_resource("planet", request_data, "planet_id", planet_id)
        response_obj = {
            "rows_affected": result,
            "planet_id": planet_id,
            "message": "record updated successfully." if result else "Error! id doesn't exist."
        }

    except ValidationError as e:
        error_msg = str(e)
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")

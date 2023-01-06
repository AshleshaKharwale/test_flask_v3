from pydantic import ValidationError
from flask import Blueprint, request, Response, json
from models.datamodels.characters import PatchCharacters
from models.datamodels.films import PatchFilms
from models.datamodels.planets import PatchPlanets
from models.datamodels.species import PatchSpecies
from models.datamodels.starships import PatchStarships
from models.datamodels.vehicles import PatchVehicles
from models.dal.dml import update_resource


patch_data = Blueprint("patch_data", __name__, url_prefix="/swapi")


def remove_none_fields(data_set):
    data = data_set.dict()
    data_copy = data.copy()
    for k, v in data.items():
        if v is None:
            data_copy.pop(k)
    return data_copy


@patch_data.patch("/people/<int:id_>")
@patch_data.patch("/people")
def patch_character(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if id_ is not None:
        request_data["char_id"] = id_

    response_obj = {}
    try:
        request_data = PatchCharacters(**request_data)
        request_data = remove_none_fields(request_data)
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


@patch_data.patch("/films/<int:id_>")
@patch_data.patch("/films")
def patch_films(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if id_ is not None:
        request_data["film_id"] = id_

    response_obj = {}
    try:
        request_data = PatchFilms(**request_data)
        request_data = remove_none_fields(request_data)
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


@patch_data.patch("/planets/<int:id_>")
@patch_data.patch("/planets")
def patch_planets(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if id_ is not None:
        request_data["planet_id"] = id_

    response_obj = {}
    try:
        request_data = PatchPlanets(**request_data)
        request_data = remove_none_fields(request_data)
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


@patch_data.patch("/species/<int:id_>")
@patch_data.patch("/species")
def patch_species(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if id_ is not None:
        request_data["species_id"] = id_

    response_obj = {}
    try:
        request_data = PatchSpecies(**request_data)
        request_data = remove_none_fields(request_data)
        species_id = request_data.pop("species_id")
        result = update_resource("species", request_data, "species_id", species_id)
        response_obj = {
            "rows_affected": result,
            "planet_id": species_id,
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


@patch_data.patch("/starships/<int:id_>")
@patch_data.patch("/starships")
def patch_starships(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if id_ is not None:
        request_data["starship_id"] = id_

    response_obj = {}
    try:
        request_data = PatchStarships(**request_data)
        request_data = remove_none_fields(request_data)
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


@patch_data.patch("/vehicles/<int:id_>")
@patch_data.patch("/vehicles")
def patch_starships(id_=None):
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if id_ is not None:
        request_data["vehicle_id"] = id_

    response_obj = {}
    try:
        request_data = PatchVehicles(**request_data)
        request_data = remove_none_fields(request_data)
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

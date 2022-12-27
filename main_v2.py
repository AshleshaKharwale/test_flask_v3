import requests
from typing import List
from multiprocessing.pool import ThreadPool
from flask import Flask, render_template
from utils.randgen import ProduceChars
from models.datamodels.characters import Characters
from models.dal.dml import insert_resource


# application instantiation
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("swapi_home.html")


@app.route("/taskone")
def task_one():
    """
    The Star Wars API lists 82 main characters in the Star Wars saga.
    This app uses a random number generator that picks a number between 1-82.
    Using these random numbers it will be pulling 15 characters from the API using Python.
    """

    home_url = "https://swapi.dev/"
    relative_url = "/api/people/{0}"  # magic string
    print(__name__)
    print("current module getting executed")

    print("[INFO] Producing 15 random characters...")
    random_chars = []
    for i in ProduceChars(1, 82):
        random_chars.append(i)
    print(f"[INFO] done - producing random 15 characters")

    output = {}

    for char in random_chars:
        abs_url = home_url + relative_url.format(char)
        print(f"fetching details from - {abs_url}  =>\n")
        response = requests.get(abs_url)
        if response.status_code != 200:
            continue
        else:
            response = response.json()
            char_data = Characters(**response)
            output.update({char: char_data.name})

            table_name = "characters"

            columns = ["name", "mass", "height", "birth_year",
                       "hair_color", "skin_color", "eye_color",
                       "gender", "homeworld"]

            values = [char_data.name, char_data.mass, char_data.height, char_data.birth_year,
                      char_data.hair_color, char_data.skin_color, char_data.eye_color,
                      char_data.gender, char_data.homeworld]
            primary_key = "char_id"

            primary_value = char

            insert_resource(table_name, primary_key, primary_value, columns, values)

    return output


@app.route("/tasktwo")
def task_two():
    """
    This app fetches data of film1 and prints names of characters, vehicles, starships, species and
    planets names.
    """
    film1_url = "https://swapi.dev/api/films/1"
    response = requests.get(film1_url)
    print(f"Fetching details from => {film1_url}\n")
    response = response.json()
    chars = response.get("characters")
    planets = response.get("planets")
    vehicles = response.get("vehicles")
    starships = response.get("starships")
    species = response.get("species")

    def fetch_name(url:str) -> str:
        """
        Hits given url and converts to json data. Extracts only name value from it.
        Returns name.
        :param url: resource url
        :return: name of resource
        """
        print(f"Fetching details from => {url}\n")
        res = requests.get(url)
        if res.status_code != 200:
            return "Not found"
        else:
            res = res.json()
        return res.get("name")

    def get_names(resource:List[str])-> List[str]:
        """
        Returns name from each resource url for given list of urls.
        :param resource: list or resource urls
        :return: list of names
        """
        pool = ThreadPool(15)
        names = pool.map(fetch_name, resource)
        return names

    char_names = get_names(chars)
    planet_names = get_names(planets)
    vehicle_names = get_names(vehicles)
    starship_names = get_names(starships)
    species_names = get_names(species)

    output = {"characters": char_names,
              "planets": planet_names,
              "vehicles": vehicle_names,
              "starships": starship_names,
              "species": species_names}

    return output


if __name__ == "__main__":
    app.run(debug=True)

import requests
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


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from starwars_task.tasks import swapi
from crud_ops.get_data import crud_app


# application instantiation
app = Flask(__name__)
app.register_blueprint(swapi)
app.register_blueprint(crud_app)


@app.route("/")
def home():
    return render_template("swapi_home.html")


if __name__ == "__main__":
    app.run(debug=True)

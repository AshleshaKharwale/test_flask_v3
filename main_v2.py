from flask import Flask, render_template
from starwars_task.tasks import swapi
from crud_ops.get_data import get_data
from crud_ops.post_data import post_data
from crud_ops.delete_data import delete_data
from crud_ops.put_data import put_data
from crud_ops.patch_data import patch_data


# application instantiation
app = Flask(__name__)
app.register_blueprint(swapi)
app.register_blueprint(get_data)
app.register_blueprint(post_data)
app.register_blueprint(delete_data)
app.register_blueprint(put_data)
app.register_blueprint(patch_data)


@app.route("/")
def home():
    return render_template("swapi_home.html")


if __name__ == "__main__":
    app.run(debug=True)

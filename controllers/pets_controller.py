from flask import render_template
from flask import Blueprint

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/clan")
def our_clan():
    return render_template("clan/index.html")

from flask import render_template
from flask import Blueprint
from models.pet import Pet
from repositories import pet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/clan")
def our_clan():
    pets = pet_repository.select_all()
    return render_template("clan/index.html", pets = pets)

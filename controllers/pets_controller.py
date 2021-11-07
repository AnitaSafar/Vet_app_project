from flask import render_template
from flask import Blueprint
from models.pet import Pet
from models.vet import Vet
from repositories import pet_repository, vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/clan")
def our_clan():
    pets = pet_repository.select_all()
    return render_template("clan/index.html", pets = pets)

@pets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets = vets)
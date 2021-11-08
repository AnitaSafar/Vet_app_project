from flask import Blueprint, render_template, redirect
from models.vet import Vet
from repositories import vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')


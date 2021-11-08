from flask import Blueprint, render_template, redirect, request
from models.vet import Vet
from repositories import vet_repository, pet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')

@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html")

@vets_blueprint.route("/vets", methods=['POST'])
def add_new_vet():
    name = request.form['name']
    specialties = request.form['specialties']
    reg_number = request.form['reg_number']

    vet = Vet(name, specialties, reg_number)
    vet_repository.save(vet)
    return redirect('/vets')
    
@vets_blueprint.route("/vets/<id>")
def show_vet(id):
    vet = vet_repository.select(id)
    pets = vet_repository.pets(vet)
    return render_template('vets/show.html', vet = vet, pets = pets)

@vets_blueprint.route("/vets/<id>/edit")
def edit_vet(id):
    vet = vet_repository.select(id)
    pets = pet_repository.select_all()
    return render_template('vets/edit.html', vet = vet, pets = pets)    

@vets_blueprint.route("/vets/<id>", methods=['POST'])
def update_vet(id):
    name = request.form['name']
    specialties = request.form['specialties']
    reg_number = request.form['reg_number']

    vet = Vet(name, specialties, reg_number, id)
    vet_repository.update(vet)
    return redirect('/vets')



from flask import render_template, request, redirect
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

@pets_blueprint.route("/register")
def register():
    vets = vet_repository.select_all()
    return render_template("clan/register.html", vets = vets)

@pets_blueprint.route("/clan", methods=['POST'])
def add_new_pet():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type = request.form['type']
    owner = request.form['owner']
    notes = request.form['notes']
    vet_id = request.form['vet_id']
    
    vet = vet_repository.select(vet_id)
    pet = Pet(name, date_of_birth, type, owner, notes, vet)
    pet_repository.save(pet)
    return redirect('/clan')

@pets_blueprint.route("/clan/<id>")
def show_pet(id):
    pet = pet_repository.select(id)
    return render_template('clan/show.html', pet = pet)

@pets_blueprint.route("/clan/<id>/edit")
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    return render_template('clan/edit.html', pet = pet, vets = vets)

@pets_blueprint.route("/clan/<id>", methods=['POST'])
def update_pet(id):
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type = request.form['type']
    owner = request.form['owner']
    notes = request.form['notes']
    vet_id = request.form['vet_id']

    vet = vet_repository.select(vet_id)
    pet = Pet(name, date_of_birth, type, owner, notes, vet, id)
    pet_repository.update(pet)
    return redirect('/clan')

@pets_blueprint.route("/clan/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/clan')

@pets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')
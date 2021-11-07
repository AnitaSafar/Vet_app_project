from db.run_sql import run_sql

from models.pet import Pet
from repositories import pet_repository, vet_repository

def save(pet):
    sql = "INSERT INTO pets (name, date_of_birth, type, owner, notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.date_of_birth, pet.type, pet.owner, pet.notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['date_of_birth'], row['type'], row['owner'], row['notes'], vet, row['id'])
        pets.append(pet)
    return pets


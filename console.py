import pdb
from models.pet import Pet
from repositories import pet_repository

pet1 = Pet("Sprinkles", "2017.08.24.", "cat", "Angela Martin", "Healthy", "John Dolittle")
pet_repository.save(pet1)

pdb.set_trace()
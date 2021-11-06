import pdb
from models.pet import Pet
from repositories import pet_repository

pet_repository.delete_all()

pet1 = Pet("Sprinkles", "2017.08.24.", "cat", "Angela Martin", "Healthy", "John Dolittle")
pet_repository.save(pet1)

pet2 = Pet("Snoopy", "1950.10.04.", "dog", "Charlie Brown", "Not an ordinary dog", "John Dolittle")
pet_repository.save(pet2)

pet_repository.select_all()


pdb.set_trace()
import pdb
from models.pet import Pet
from models.vet import Vet
from repositories import pet_repository, vet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("John Dolittle")
vet_repository.save(vet1)

vet2 = Vet("Stephen Strange")
vet_repository.save(vet2)

vet_repository.select_all()

pet1 = Pet("Sprinkles", "2017/08/24", "cat", "Angela Martin", "Healthy", vet1)
pet_repository.save(pet1)

pet2 = Pet("Snoopy", "1950/10/04", "dog", "Charlie Brown", "Not an ordinary dog", vet2)
pet_repository.save(pet2)

pet_repository.select_all()




pdb.set_trace()
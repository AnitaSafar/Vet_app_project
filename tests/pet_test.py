import unittest
from models.pet import Pet

class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet("Sprinkles", "2017.08.24.", "cat", "Angela Martin", "Healthy", "John Dolittle")

    def test_pet_has_name(self):
        self.assertEqual("Sprinkles", self.pet.name)

    def test_pet_has_dob(self):
        self.assertEqual("2017.08.24.", self.pet.date_of_birth)

    def test_pet_has_type(self):
        self.assertEqual("cat", self.pet.type)

    def test_pet_has_owner(self):
        self.assertEqual("Angela Martin", self.pet.owner)

    def test_pet_has_notes(self):
        self.assertEqual("Healthy", self.pet.notes)

    def test_pet_has_vet(self):
        self.assertEqual("John Dolittle", self.pet.vet)
        
    def test_pet_has_id(self):
        self.assertEqual(None, self.pet.id)
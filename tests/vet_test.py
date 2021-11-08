import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("John Dolittle", "Psychiatry", 3147)

    def test_vet_has_name(self):
        self.assertEqual("John Dolittle", self.vet.name)

    def test_vet_has_id(self):
        self.assertEqual(None, self.vet.id)

    def test_vet_has_specialties(self):
        self.assertEqual("Psychiatry", self.vet.specialties)

    def test_vet_has_reg_number(self):
        self.assertEqual(3147, self.vet.reg_number)
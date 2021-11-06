import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):
    def setUp(self):
        self.vet = Vet("John Dolittle")

    def test_vet_has_name(self):
        self.assertEqual("John Dolittle", self.vet.name)

    def test_vet_has_id(self):
        self.assertEqual(None, self.vet.id)
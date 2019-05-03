import unittest
from entities import races, empire, city
from entities.buildings import barrack
from entities.units import scout, warrior
from entities.units import builder


class TestBarrack(unittest.TestCase):
    def setUp(self) -> None:
        self.city = city.City("Forut", empire.Empire(races.orcs))
        self.barrack = barrack.OrcsBarrack(health=10, city=self.city)

    def test_default(self):
        self.assertEqual(self.barrack.race, races.orcs)
        self.assertEqual(self.barrack.health, 10)
        self.assertEqual(self.barrack._master_city, self.city)

    def test_create_builder(self):
        self.assertTrue(isinstance(self.barrack.create_builder(), builder.Builder))

    def test_create_scout(self):
        self.assertTrue(isinstance(self.barrack.create_scout(), scout.Scout))

    def test_create_warrior(self):
        self.assertTrue(isinstance(self.barrack.create_warrior(), warrior.Warrior))
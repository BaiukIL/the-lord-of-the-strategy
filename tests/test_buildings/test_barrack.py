import unittest
from game_objects import races, empire, city
from game_objects.buildings import barrack
from game_objects.units import scout, warrior
from game_objects.units import builder


class TestBarrack(unittest.TestCase):
    def setUp(self) -> None:
        self.city = city.City("Forut", empire.Empire(races.ORCS))
        self.barrack = barrack.OrcsBarrack(health=10, city=self.city)

    def test_default(self):
        self.assertEqual(self.barrack.race, races.ORCS)
        self.assertEqual(self.barrack.health, 10)
        self.assertEqual(self.barrack._master_city, self.city)

    def test_create_builder(self):
        self.assertTrue(isinstance(self.barrack.create_builder(), builder.Builder))

    def test_create_scout(self):
        self.assertTrue(isinstance(self.barrack.create_scout(), scout.Scout))

    def test_create_warrior(self):
        self.assertTrue(isinstance(self.barrack.create_warrior(), warrior.Warrior))
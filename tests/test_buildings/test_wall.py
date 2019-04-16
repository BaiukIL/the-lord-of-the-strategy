import unittest
from abstraction import races, empire, city
from abstraction.buildings import wall


class TestBarrack(unittest.TestCase):
    def setUp(self) -> None:
        self.city = city.City("Fax", empire.Empire(races.elves))
        self.wall = wall.Wall(health=10, city=self.city)

    def test_default(self):
        self.assertEqual(self.wall.race, races.elves)
        self.assertEqual(self.wall.health, 10)
        self.assertEqual(self.wall._master_city, self.city)

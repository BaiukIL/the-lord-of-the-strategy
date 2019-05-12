import unittest
from game_objects import races, empire, city
from game_objects.buildings import mine


class TestBarrack(unittest.TestCase):
    def setUp(self) -> None:
        self.city = city.City("Pogeet", empire.Empire(races.DWARFS))
        self.mine = mine.Mine(health=10, city=self.city)

    def test_default(self):
        self.assertEqual(self.mine.race, races.DWARFS)
        self.assertEqual(self.mine.health, 10)
        self.assertEqual(self.mine._master_city, self.city)

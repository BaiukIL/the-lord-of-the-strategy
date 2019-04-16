import unittest
from abstraction import races, empire, city
from abstraction.buildings import fabric
from abstraction.buildings import barrack, mine, wall


class TestFabric(unittest.TestCase):
    def setUp(self) -> None:
        self.city = city.City("Forut", empire.Empire(races.orcs))
        self.fabric = fabric.Manufacture().create_fabric(self.city)

    def test_default(self):
        self.assertEqual(self.fabric._master_city, self.city)

    def test_build_barrack(self):
        self.assertTrue(isinstance(self.fabric.build_barrack(), barrack.OrcsBarrack))

    def test_build_mine(self):
        self.assertTrue(isinstance(self.fabric.build_mine(), mine.Mine))

    def test_build_wall(self):
        self.assertTrue(isinstance(self.fabric.build_wall(), wall.Wall))

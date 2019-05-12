import unittest
from game_objects import races, empire, city
from game_objects.buildings import fabric
from game_objects.buildings import barrack, mine, wall


class TestCity(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ORCS)
        self.city = city.City("Forut", self.empire)

    def test_default(self):
        self.assertEqual(self.city._master_empire, self.empire)
        self.assertEqual(self.city.race, races.ORCS)
        self.assertEqual(self.city.name, "Forut")
        self.assertEqual(len(self.city.buildings), 0)
        self.assertTrue(isinstance(self.city._fabric, fabric.OrcsFabric))

    def test_building_creation_and_deletion(self):
        wall1 = self.city.build_wall()
        barrack1 = self.city.build_barrack()
        mine1 = self.city.build_mine()
        mine2 = self.city.build_mine()

        self.assertEqual(wall1.race, races.ORCS)
        self.assertTrue(isinstance(wall1, wall.Wall))
        self.assertEqual(barrack1.race, races.ORCS)
        self.assertTrue(isinstance(barrack1, barrack.OrcsBarrack))
        self.assertEqual(mine1.race, races.ORCS)
        self.assertTrue(isinstance(mine1, mine.Mine))
        self.assertEqual(mine2.race, races.ORCS)
        self.assertTrue(isinstance(mine2, mine.Mine))

        self.assertIn(wall1, self.city.buildings)
        self.assertIn(barrack1, self.city.buildings)
        self.assertIn(mine1, self.city.buildings)
        self.assertIn(mine2, self.city.buildings)

        self.city.remove_building(wall1)
        self.assertNotIn(wall1, self.city.buildings)
        self.assertRaises(city.CityError, lambda: self.city.remove_building(wall1))

        self.city.remove_building(mine1)
        self.assertNotIn(wall1, self.city.buildings)
        self.assertRaises(city.CityError, lambda: self.city.remove_building(mine1))

        self.assertIn(mine2, self.city.buildings)
        self.city.remove_building(mine2)
        self.assertNotIn(wall1, self.city.buildings)
        self.assertRaises(city.CityError, lambda: self.city.remove_building(mine2))

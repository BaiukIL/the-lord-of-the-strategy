import unittest
from abstraction import races, empire, city
from abstraction.buildings import fabric
from abstraction.buildings import barrack, mine, wall


class TestCity(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.orcs)
        self.city = city.City("Forut", self.empire)

    def test_default(self):
        self.assertEqual(self.city._master_empire, self.empire)
        self.assertEqual(self.city.race, races.orcs)
        self.assertEqual(self.city.name, "Forut")
        self.assertEqual(len(self.city._buildings), 0)
        self.assertTrue(isinstance(self.city._fabric, fabric.OrcsFabric))

    def test_building_creation_and_deletion(self):
        wall1 = self.city.build_wall()
        barrack1 = self.city.build_barrack()
        mine1 = self.city.build_mine()
        mine2 = self.city.build_mine()

        self.assertEqual(wall1.race, races.orcs)
        self.assertTrue(isinstance(wall1, wall.Wall))
        self.assertEqual(barrack1.race, races.orcs)
        self.assertTrue(isinstance(barrack1, barrack.OrcsBarrack))
        self.assertEqual(mine1.race, races.orcs)
        self.assertTrue(isinstance(mine1, mine.Mine))
        self.assertEqual(mine2.race, races.orcs)
        self.assertTrue(isinstance(mine2, mine.Mine))

        self.assertIn(wall1, self.city._buildings)
        self.assertIn(barrack1, self.city._buildings)
        self.assertIn(mine1, self.city._buildings)
        self.assertIn(mine2, self.city._buildings)

        self.city.remove_building(wall1)
        self.assertNotIn(wall1, self.city._buildings)
        self.assertRaises(city.CityError, lambda: self.city.remove_building(wall1))

        self.city.remove_building(mine1)
        self.assertNotIn(wall1, self.city._buildings)
        self.assertRaises(city.CityError, lambda: self.city.remove_building(mine1))

        self.assertIn(mine2, self.city._buildings)
        self.city.remove_building(mine2)
        self.assertNotIn(wall1, self.city._buildings)
        self.assertRaises(city.CityError, lambda: self.city.remove_building(mine2))

import unittest
from interface.interface import Interface
from game import Game
from game_objects import races, empire
from game_objects.buildings import fabric
from game_objects.buildings import barrack, mine, wall


class TestCity(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ORCS)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)
        self.city = self.empire.set_city(name='test city', cost=50)

    def test_default(self):
        self.assertEqual(self.city.empire, self.empire)
        self.assertEqual(self.city.name, 'test city')
        self.assertEqual(len(self.city.buildings), 0)
        self.assertTrue(isinstance(self.city._fabric, fabric.OrcsFabric))

    def test_building_creation_and_deletion(self):
        wall1 = self.city.build_wall((300, 0))
        barrack1 = self.city.build_barrack((300, 300))
        mine1 = self.city.build_mine((0, 300))
        mine2 = self.city.build_mine((700, 700))

        self.assertEqual(wall1.empire, self.empire)
        self.assertTrue(isinstance(wall1, wall.Wall))
        self.assertEqual(barrack1.empire, self.empire)
        self.assertTrue(isinstance(barrack1, barrack.OrcsBarrack))
        self.assertEqual(mine1.empire, self.empire)
        self.assertTrue(isinstance(mine1, mine.Mine))
        self.assertEqual(mine2.empire, self.empire)
        self.assertTrue(isinstance(mine2, mine.Mine))

        self.assertIn(wall1, self.city.buildings)
        self.assertIn(barrack1, self.city.buildings)
        self.assertIn(mine1, self.city.buildings)
        self.assertIn(mine2, self.city.buildings)

        wall1.kill()
        self.assertNotIn(wall1, self.city.buildings)

        wall1.kill()
        self.assertNotIn(wall1, self.city.buildings)

        self.assertIn(mine2, self.city.buildings)

import unittest
from interface.interface import Interface
from game import Game
from game_objects import races, empire
from game_objects.buildings import fabric
from game_objects.buildings import barrack, mine, wall


class TestFabric(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ORCS)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)
        self.fabric = fabric.Manufacture().create_fabric(self.empire)

    def test_default(self):
        self.assertEqual(self.fabric.empire, self.empire)

    def test_build_barrack(self):
        barrack_ = self.fabric.build_barrack((500, 500))
        self.assertTrue(isinstance(barrack_, barrack.OrcsBarrack))
        self.assertTrue(barrack_.cost, 20)
        self.assertTrue(barrack_.health, 15)

    def test_build_mine(self):
        mine_ = self.fabric.build_mine((500, 500))
        self.assertTrue(isinstance(mine_, mine.Mine))
        self.assertTrue(mine_.cost, 10)
        self.assertTrue(mine_.health, 10)
        self.assertTrue(mine_.reload, 60)

    def test_build_wall(self):
        wall_ = self.fabric.build_wall((500, 500))
        self.assertTrue(isinstance(wall_, wall.Wall))
        self.assertTrue(wall_.cost, 5)
        self.assertTrue(wall_.health, 10)

    def tearDown(self) -> None:
        for obj in Game().objects:
            obj.kill()

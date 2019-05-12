import unittest
from interface.interface import Interface
from game import Game
from game_objects import races, empire
from game_objects.units import scout, warrior
from game_objects.units import builder


class TestBarrack(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ORCS, start_resources=100)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)
        self.barrack = self.empire.set_city(name='test city').build_barrack(mouse_pos=(500, 500))
        self.assertEqual(self.empire.resources, 80)

    def test_default(self):
        self.assertEqual(self.barrack.empire, self.empire)
        self.assertEqual(self.barrack.cost, 20)
        self.assertEqual(self.barrack.health, 15)

    def test_create_builder(self):
        builder_ = self.barrack.create_builder()
        self.assertTrue(isinstance(builder_, builder.Builder))
        self.assertTrue(builder_.cost, 5)
        self.assertTrue(builder_.health, 2)
        self.assertTrue(builder_.max_speed, 6)

    def test_create_scout(self):
        scout_ = self.barrack.create_scout()
        self.assertTrue(isinstance(scout_, scout.Scout))
        self.assertTrue(scout_.cost, 8)
        self.assertTrue(scout_.health, 3)
        self.assertTrue(scout_.damage, 2)
        self.assertTrue(scout_.max_speed, 6)

    def test_create_warrior(self):
        warrior_ = self.barrack.create_scout()
        self.assertTrue(isinstance(warrior_, warrior.Warrior))
        self.assertTrue(warrior_.cost, 10)
        self.assertTrue(warrior_.health, 5)
        self.assertTrue(warrior_.damage, 4)
        self.assertTrue(warrior_.max_speed, 3)

    def tearDown(self) -> None:
        # see test_units.TestWarrior tearDown
        for obj in Game().objects:
            obj.kill()


class TestMine(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ORCS, start_resources=100)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)
        self.mine = self.empire.set_city(name='test city').build_mine(mouse_pos=(500, 500))

    def test_default(self):
        self.assertEqual(self.mine.empire, self.empire)
        self.assertEqual(self.mine.cost, 10)
        self.assertEqual(self.mine.health, 10)
        self.assertEqual(self.mine.reload, 60)

    def test_mine(self):
        self.mine.mine()
        self.assertEqual(self.empire.resources, 95)
        self.mine.mine()
        self.assertEqual(self.empire.resources, 100)

    def tearDown(self) -> None:
        for obj in Game().objects:
            obj.kill()

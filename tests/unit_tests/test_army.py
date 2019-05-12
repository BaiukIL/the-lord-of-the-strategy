import unittest
from interface.interface import Interface
from game import Game
from game_objects import races, empire, army
from game_objects.units import unit


class TestArmy(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.DWARFS)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)
        self.army = army.Army(empire=self.empire)

    def test_default(self):
        self.assertEqual(self.army.empire, self.empire)
        self.assertEqual(self.army.size(), 0)

    def test_recruit(self):
        self.army.recruit_unit(unit.Unit(self.empire, 10, 10, 10, (10, 10), None))
        self.army.recruit_unit(unit.Unit(self.empire, 11, 10, 10, (10, 10), None))
        self.army.recruit_unit(unit.Unit(self.empire, 10, 11, 10, (10, 10), None))
        self.assertEqual(self.army.size(), 3)

    def test_remove(self):
        unit1 = unit.Unit(self.empire, 10, 10, 10, (10, 10), None)
        unit2 = unit.Unit(self.empire, 10, 11, 10, (10, 10), None)
        unit3 = unit.Unit(self.empire, 10, 10, 11, (10, 10), None)
        leaf = army.ArmyLeaf(unit1)
        self.army.recruit_unit(unit1)
        self.army.recruit_unit(unit2)
        self.army.recruit_unit(unit3)
        self.army.remove_group(leaf)
        self.assertEqual(self.army.size(), 3)

    def tearDown(self) -> None:
        for obj in Game().objects:
            obj.kill()

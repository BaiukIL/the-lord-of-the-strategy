import unittest
from game_objects import races, empire, army, unit


class TestArmy(unittest.TestCase):
    def setUp(self) -> None:
        self.army = army.Army(empire.Empire(races.DWARFS))

    def test_default(self):
        self.assertEqual(self.army.race, races.DWARFS)
        self.assertEqual(self.army.size(), 0)

    def test_recruit(self):
        self.army.recruit_unit(unit.Unit(races.ELVES, 10, 10))
        self.army.recruit_unit(unit.Unit(races.ELVES, 10, 10))
        self.army.recruit_unit(unit.Unit(races.ELVES, 10, 10))
        self.assertEqual(self.army.size(), 3)

    # def test_remove_group(self):
    #     self.army.remove_group()
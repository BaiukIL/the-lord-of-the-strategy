import unittest
from entities import races, empire, army
from entities.units import unit


class TestArmy(unittest.TestCase):
    def setUp(self) -> None:
        self.army = army.Army(empire.Empire(races.dwarfs))

    def test_default(self):
        self.assertEqual(self.army.race, races.dwarfs)
        self.assertEqual(self.army.size(), 0)

    def test_recruit(self):
        self.army.recruit_unit(unit.Unit(races.elves, 10, 10))
        self.army.recruit_unit(unit.Unit(races.elves, 10, 10))
        self.army.recruit_unit(unit.Unit(races.elves, 10, 10))
        self.assertEqual(self.army.size(), 3)

    # def test_remove_group(self):
    #     self.army.remove_group()
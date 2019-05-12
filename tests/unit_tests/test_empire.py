import unittest
from interface.interface import Interface
from game import Game
from game_objects import races, empire, army


class TestEmpire(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ORCS)
        self.other_empire = empire.Empire(races.ELVES)
        Interface(self.empire, self.other_empire)
        Game(self.empire, self.other_empire)

    def test_default(self):
        self.assertEqual(self.empire.race, races.ORCS)
        self.assertEqual(self.empire.name, "DefaultEmpireName")
        self.assertTrue(isinstance(self.empire.army, army.Army))
        self.assertEqual(len(self.empire.cities), 0)

    def test_default_with_custom_name(self):
        new_empire = empire.Empire(races.DWARFS, "My Empire")
        self.assertEqual(new_empire.race, races.DWARFS)
        self.assertEqual(new_empire.name, "My Empire")

    def test_set_city(self):
        city1 = self.empire.set_city("Livur")
        self.assertTrue(self.empire.cities.has(city1))
        city2 = self.empire.set_city("Yoigh")
        self.assertTrue(self.empire.cities.has(city2))
        self.assertRaises(empire.EmpireError, lambda: self.empire.set_city("Livur"))
        self.assertRaises(empire.EmpireError, lambda: self.empire.set_city("Yoigh"))

    def test_get_city(self):
        self.assertRaises(empire.EmpireError, lambda: self.empire.get_city("ert"))
        self.empire.set_city("Livur")

        self.assertIn(self.empire.get_city("Livur"), self.empire.cities)
        self.assertEqual(self.empire.get_city("Livur").name, "Livur")
        self.empire.set_city("Yoigh")
        self.assertIn(self.empire.get_city("Yoigh"), self.empire.cities)
        self.assertEqual(self.empire.get_city("Yoigh").name, "Yoigh")

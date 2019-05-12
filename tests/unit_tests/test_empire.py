import unittest
from game_objects import races, empire, army


class TestEmpire(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(races.ELVES)

    def test_default(self):
        self.assertEqual(self.empire.race, races.ELVES)
        self.assertEqual(self.empire.name, "DefaultEmpireName")
        self.assertTrue(isinstance(self.empire.army, army.Army))
        self.assertEqual(len(self.empire.cities), 0)

    def test_default_with_custom_name(self):
        new_empire = empire.Empire(races.DWARFS, "My Empire")
        self.assertEqual(new_empire.race, races.DWARFS)
        self.assertEqual(new_empire.name, "My Empire")

    def test_set_city(self):
        self.empire.set_city("Livur")
        self.assertIn("Livur", self.empire.cities)
        self.empire.set_city("Yoigh")
        self.assertIn("Yoigh", self.empire.cities)
        self.assertRaises(empire.EmpireError, lambda: self.empire.set_city("Livur"))
        self.assertRaises(empire.EmpireError, lambda: self.empire.set_city("Yoigh"))

    def test_get_city(self):
        self.assertRaises(empire.EmpireError, lambda: self.empire.get_city("ert"))
        self.empire.set_city("Livur")

        self.assertEqual(self.empire.get_city("Livur"), self.empire.cities["Livur"])
        self.assertEqual(self.empire.get_city("Livur").name, "Livur")
        self.empire.set_city("Yoigh")
        self.assertEqual(self.empire.get_city("Yoigh"), self.empire.cities["Yoigh"])
        self.assertEqual(self.empire.get_city("Livur"), self.empire.cities["Livur"])
        self.assertEqual(self.empire.get_city("Yoigh").name, "Yoigh")

    def test_destroy_city(self):
        self.assertRaises(empire.EmpireError, lambda: self.empire.destroy_city("aww"))

        self.empire.set_city("Livur")
        self.empire.set_city("Yoigh")
        self.assertRaises(empire.EmpireError, lambda: self.empire.destroy_city("weeer"))

        self.empire.destroy_city("Livur")
        self.assertRaises(empire.EmpireError, lambda: self.empire.get_city("Livur"))
        self.assertRaises(empire.EmpireError, lambda: self.empire.destroy_city("Livur"))

        self.empire.set_city("Livur")
        self.assertEqual(self.empire.get_city("Livur").name, "Livur")
        self.empire.destroy_city("Livur")

        self.empire.destroy_city("Yoigh")
        self.assertRaises(empire.EmpireError, lambda: self.empire.destroy_city("Yoigh"))
        self.assertRaises(empire.EmpireError, lambda: self.empire.get_city("Yoigh"))

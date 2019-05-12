import unittest
from trash.object_properties import damage


class TestHealth(unittest.TestCase):
    def setUp(self) -> None:
        self.damage = damage.Damage(10)

    def test_default(self):
        self.assertEqual(self.damage.damage, 10)
        new_damage = damage.Damage(-1)
        self.assertEqual(new_damage.damage, 0)

    def test_decrease(self):
        self.damage.decrease_damage(4)
        self.assertEqual(self.damage.damage, 6)
        self.damage.decrease_damage(4)
        self.assertEqual(self.damage.damage, 2)
        self.damage.decrease_damage(0)
        self.assertEqual(self.damage.damage, 2)

        self.assertRaises(damage.DamageError, lambda: self.damage.decrease_damage(-2))

        self.damage.decrease_damage(2)
        self.assertEqual(0, 0)
        self.assertFalse(self.damage.can_hit())
        self.damage.decrease_damage(2)
        self.assertEqual(0, 0)
        self.assertFalse(self.damage.can_hit())

    def test_increase(self):
        self.damage.increase_damage(0)
        self.assertEqual(self.damage.damage, 10)
        self.damage.increase_damage(10)
        self.assertEqual(self.damage.damage, 20)

        self.assertRaises(damage.DamageError, lambda: self.damage.increase_damage(-2))
        self.assertTrue(self.damage.can_hit())

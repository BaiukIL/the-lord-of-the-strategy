import unittest
from entities.object_properties import health


# Health, but not abstract (for testing only)
class NonAbstractHealth(health.Health):
    def _destroy(self):
        pass


class TestHealth(unittest.TestCase):
    def setUp(self) -> None:
        self.health = NonAbstractHealth(10)

    def test_default(self):
        self.assertEqual(self.health.health, 10)
        self.assertRaises(health.HealthError, lambda: NonAbstractHealth(0))
        self.assertRaises(health.HealthError, lambda: NonAbstractHealth(-5))

    def test_decrease(self):
        self.health.decrease_health(4)
        self.assertEqual(self.health.health, 6)
        self.health.decrease_health(4)
        self.assertEqual(self.health.health, 2)
        self.health.decrease_health(0)
        self.assertEqual(self.health.health, 2)

        self.assertRaises(health.HealthError, lambda: self.health.decrease_health(-2))

        self.health.decrease_health(2)
        self.assertEqual(0, 0)
        self.assertFalse(self.health.is_alive())

    def test_increase(self):
        self.health.increase_health(0)
        self.assertEqual(self.health.health, 10)
        self.health.increase_health(10)
        self.assertEqual(self.health.health, 20)

        self.assertRaises(health.HealthError, lambda: self.health.increase_health(-2))
        self.assertTrue(self.health.is_alive())

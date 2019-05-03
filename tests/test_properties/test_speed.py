import unittest
from entities.object_properties import speed


class TestHealth(unittest.TestCase):
    def setUp(self) -> None:
        self.speed = speed.Speed(10)

    def test_default(self):
        self.assertEqual(self.speed.speed, 10)
        new_speed = speed.Speed(-1)
        self.assertEqual(new_speed.speed, 0)

    def test_decrease(self):
        self.speed.decrease_speed(4)
        self.assertEqual(self.speed.speed, 6)
        self.speed.decrease_speed(4)
        self.assertEqual(self.speed.speed, 2)
        self.speed.decrease_speed(0)
        self.assertEqual(self.speed.speed, 2)

        self.assertRaises(speed.SpeedError, lambda: self.speed.decrease_speed(-2))

        self.speed.decrease_speed(2)
        self.assertEqual(0, 0)
        self.assertFalse(self.speed.can_move())
        self.speed.decrease_speed(2)
        self.assertEqual(0, 0)
        self.assertFalse(self.speed.can_move())

    def test_increase(self):
        self.speed.increase_speed(0)
        self.assertEqual(self.speed.speed, 10)
        self.speed.increase_speed(10)
        self.assertEqual(self.speed.speed, 20)

        self.assertRaises(speed.SpeedError, lambda: self.speed.increase_speed(-2))
        self.assertTrue(self.speed.can_move())

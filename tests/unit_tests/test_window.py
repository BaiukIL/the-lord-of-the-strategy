import unittest
import pygame
from interface import window
import configs


class TestWindow(unittest.TestCase):
    def setUp(self) -> None:
        self.window = window.Window((10, 10))

    def test_default(self):
        win = window.Window((10, 10), image=pygame.Surface((100, 100)))
        win.set_default_alpha(150)
        self.assertEqual(win.real_image, win.image)
        self.assertEqual(win.real_image, win._draw_image)
        self.assertEqual(win.rect.size, (10, 10))
        self.assertTrue(isinstance(win._state, window.PassiveWindowState))
        self.assertEqual(win._hint_message, None)
        self.assertEqual(win._default_alpha, 150)
        self.assertEqual(win.image.get_alpha(), 150)
        self.assertFalse(win._bordered)
        self.assertFalse(win._constant_bordered)
        self.assertFalse(win._never_bordered)
        self.assertEqual(win._borders_size, configs.BORDERS_SIZE)
        self.assertEqual(win._borders_color, configs.BORDERS_COLOR)

    def test_borders(self):
        self.window.add_borders()
        self.assertTrue(self.window._bordered)
        self.assertNotEqual(self.window.image, self.window.real_image)
        self.window.add_borders()
        self.assertTrue(self.window._bordered)
        self.assertNotEqual(self.window.image, self.window.real_image)
        self.window.remove_borders()
        self.assertFalse(self.window._bordered)
        self.assertEqual(self.window.image, self.window.real_image)
        self.window.set_constant_bordered()
        self.assertRaises(window.WindowError, lambda: self.window.set_never_bordered())
        self.window.remove_borders()
        self.assertTrue(self.window._bordered)
        self.assertNotEqual(self.window.image, self.window.real_image)

    def test_image(self):
        img = self.window.real_image
        self.window.set_temporary_image(pygame.Surface((100, 100)), delay=3)
        self.assertNotEqual(self.window.image, self.window.real_image)
        self.assertNotEqual(self.window.image, img)
        self.window.clear()

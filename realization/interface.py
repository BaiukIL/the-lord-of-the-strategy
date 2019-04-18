import pygame


class Interface:
    selected: pygame.Surface

    def __init__(self):
        self._objects = pygame.sprite.Group()
        self.selected = pygame

    def draw(self, surface: pygame.Surface):
        self._objects.draw(surface)
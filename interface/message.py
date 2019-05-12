import pygame
import time
from typing import *


class Message(pygame.sprite.Sprite):
    def __init__(self, text: Text, lifetime: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        indent = 25
        line_pos = [0, 0]
        font = pygame.font.SysFont(name='freesansbold.ttf', size=40)
        for line in text.split('\n'):
            self.image.blit(font.render(line, True, pygame.Color('red')), line_pos)
            line_pos[1] += indent

        self.start_time = time.time()
        self.lifetime = lifetime

    def update(self, *args):
        if time.time() - self.start_time > self.lifetime:
            self.kill()

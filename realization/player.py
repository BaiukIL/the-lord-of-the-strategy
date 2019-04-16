import pygame
from realization import gameconfig


class Player(pygame.sprite.Sprite):
    def __init__(self, world_map: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 30
        self.camera = pygame.Rect((0, 0), gameconfig.SCR_SIZE)
        self.map = world_map

    def move(self, key, mouse_pos):
        if key[pygame.K_w] or mouse_pos[1] == self.camera.top:  # Check key
            self.camera.y -= self.speed
        if key[pygame.K_s] or mouse_pos[1] == self.camera.bottom - 1:
            self.camera.y += self.speed
        if key[pygame.K_a] or mouse_pos[0] == self.camera.left:
            self.camera.x -= self.speed
        if key[pygame.K_d] or mouse_pos[0] == self.camera.right - 1:
            self.camera.x += self.speed
        self._fix_map_collision()

    def _fix_map_collision(self):
        world_rect = self.map.get_rect()
        if self.camera.left < 0:  # Check map borders collision
            self.camera.left = 0
        elif self.camera.right > world_rect.right:
            self.camera.right = world_rect.right
        if self.camera.bottom > world_rect.bottom:
            self.camera.bottom = world_rect.bottom
        elif self.camera.top < 0:
            self.camera.top = 0

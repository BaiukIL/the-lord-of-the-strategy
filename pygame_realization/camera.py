import pygame
from configs import interface_config


class Camera(pygame.Rect):
    def __init__(self, world_map: pygame.Rect):
        super().__init__(interface_config.CAMERA_START_POS, interface_config.SCR_SIZE)
        self._speed = interface_config.CAMERA_SPEED
        self._map = world_map

    def move_view(self, key, mouse_pos):
        if key[pygame.K_w] or mouse_pos[1] == 0:
            self.y -= self._speed
        if key[pygame.K_s] or mouse_pos[1] == interface_config.SCR_HEIGHT - 1:
            self.y += self._speed
        if key[pygame.K_a] or mouse_pos[0] == 0:
            self.x -= self._speed
        if key[pygame.K_d] or mouse_pos[0] == interface_config.SCR_WIDTH - 1:
            self.x += self._speed
        self._fix_collision_with_map()

    # Check map borders collision
    def _fix_collision_with_map(self):
        if self.left < 0:
            self.left = 0
        elif self.right > self._map.right:
            self.right = self._map.right
        if self.bottom > self._map.bottom:
            self.bottom = self._map.bottom
        elif self.top < 0:
            self.top = 0

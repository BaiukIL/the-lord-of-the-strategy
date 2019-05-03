import pygame
from configs import interface_config


class Camera(pygame.Rect):
    def __init__(self, world_map: pygame.Surface):
        super().__init__(interface_config.CAMERA_START_POS, interface_config.SCR_SIZE)
        self.speed = interface_config.CAMERA_SPEED
        self.map = world_map

    def move_view(self, key, mouse_pos):
        if key[pygame.K_w] or mouse_pos[1] == self.top:
            self.y -= self.speed
        if key[pygame.K_s] or mouse_pos[1] == self.bottom - 1:
            self.y += self.speed
        if key[pygame.K_a] or mouse_pos[0] == self.left:
            self.x -= self.speed
        if key[pygame.K_d] or mouse_pos[0] == self.right - 1:
            self.x += self.speed
        self._fix_collision_with_map()

    # Check map borders collision
    def _fix_collision_with_map(self):
        world_rect = self.map.get_rect()
        if self.left < 0:
            self.left = 0
        elif self.right > world_rect.right:
            self.right = world_rect.right
        if self.bottom > world_rect.bottom:
            self.bottom = world_rect.bottom
        elif self.top < 0:
            self.top = 0

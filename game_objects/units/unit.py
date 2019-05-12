"""This is base class for all units"""


import pygame
from abc import ABC
from typing import Tuple, Text
# project modules #
from game_objects import base_object


def distance_between_points(one, other) -> float:
    return pygame.math.Vector2(one).distance_to(pygame.math.Vector2(other))


class Unit(base_object.GameObject, ABC):
    def __init__(self, empire, health: int, speed: int, cost: int, size: Tuple[int, int], image: pygame.Surface):
        assert speed >= 0
        base_object.GameObject.__init__(self, empire=empire, health=health, cost=cost, size=size, image=image)
        self.max_speed = speed
        self.speed = pygame.math.Vector2()
        self.cur_real_pos = list(self.rect.center)
        self.destination = self.rect.center

    def update_position(self):
        self.destination = self.rect.center
        self.cur_real_pos = list(self.rect.center)

    def set_move_to(self, dest: Tuple[int, int]):
        self.destination = dest
        self.cur_real_pos = list(self.rect.center)
        self.speed = pygame.math.Vector2(dest) - pygame.math.Vector2(self.rect.center)
        if self.speed.length() > 0:
            self.speed.scale_to_length(self.max_speed)

    def move(self):
        previous_pos = self.rect.center
        all_intersected = pygame.sprite.Group()
        if abs(self.rect.centerx - self.destination[0]) >= self.max_speed or abs(
                self.rect.centery - self.destination[1]) >= self.max_speed:
            self.cur_real_pos[0] += self.speed.x
            self.rect.centerx = self.cur_real_pos[0]
            intersected = pygame.sprite.spritecollide(self, self._all_objects, False)
            intersected.remove(self)
            all_intersected.add(intersected)
            for obj in intersected:
                if self.speed.x < 0:
                    self.rect.left = obj.rect.right
                else:
                    self.rect.right = obj.rect.left
                self.cur_real_pos[0] = self.rect.centerx

            self.cur_real_pos[1] += self.speed.y
            self.rect.centery = self.cur_real_pos[1]
            intersected = pygame.sprite.spritecollide(self, self._all_objects, False)
            intersected.remove(self)
            all_intersected.add(intersected)
            for obj in intersected:
                if self.speed.y < 0:
                    self.rect.top = obj.rect.bottom
                else:
                    self.rect.bottom = obj.rect.top
                self.cur_real_pos[1] = self.rect.centery
        # if unit got stuck
        if self.rect.center == previous_pos:
            self.action_while_stuck(all_intersected)

    def stop_move(self):
        self.set_move_to(self.rect.center)

    # inherited methods
    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.set_move_to(mouse_pos)

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        result += "Speed: {}\n".format(self.max_speed)
        return result

    def action_while_update(self):
        if self.speed.length() != 0:
            self.move()

    # empty methods
    def action_while_stuck(self, intersected: pygame.sprite.Group):
        pass

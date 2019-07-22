""" This module contains `AttackUnit` - a base class for units which are able to attack. """


import time
from abc import ABC
from typing import Tuple, Text
import pygame
# project modules #
from game_objects.units.unit import Unit


class AttackUnit(Unit, ABC):
    """ An attack unit base class. """

    def __init__(self,
                 empire,
                 health: int,
                 speed: int,
                 damage: int,
                 fight_distance: int,
                 cost: int,
                 size: Tuple[int, int],
                 image: pygame.Surface):

        Unit.__init__(self,
                      empire=empire,
                      size=size,
                      image=image,
                      health=health,
                      speed=speed,
                      cost=cost)

        self.damage = damage
        self.fight_distance = fight_distance
        self.attack_target = pygame.sprite.GroupSingle()
        self.attack_delay = 3  # time in seconds
        self._last_attack_time = time.time()

    def attack(self, obj):
        if time.time() - self._last_attack_time > self.attack_delay:
            obj.decrease_health(self.damage)
            self._last_attack_time = time.time()

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.attack_target.empty()
        self.set_move_to(mouse_pos)

    def interact_with(self, obj):
        if obj.empire is not self.empire:
            self.attack_target.add(obj)

    def info(self) -> Text:
        result = ''
        result += f'Race: {self.empire.race}\n'
        result += f'Empire: {self.empire.name}\n'
        result += f'Health: {self.health}\n'
        result += f'Speed: {self.max_speed}\n'
        result += f'Damage: {self.damage}\n'
        return result

    def action_while_update(self):
        self.set_move_to(self.destination)
        for target in self.attack_target:
            if self.is_on_attack_distance_to(target):
                self.attack(target)
                return
            self.set_move_to(target.rect.center)
        self.move()

    def action_while_stuck(self, intersected: pygame.sprite.Group):
        """ Chooses a collided object as attack target. """
        for obj in intersected:
            if obj.empire is not self.empire:
                self.attack_target.add(obj)
                return

    def is_on_attack_distance_to(self, target):
        return _distance_between_points(self.rect.center, target.rect.center) < self.fight_distance


def _distance_between_points(point1, point2) -> float:
    return pygame.math.Vector2(point1).distance_to(pygame.math.Vector2(point2))

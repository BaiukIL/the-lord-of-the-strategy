""" This module contains `Unit` which is a base class for all units. """


from abc import ABC
from typing import Tuple, Text
import pygame
# project modules #
from game_objects import base_object


class Unit(base_object.GameObject, ABC):
    """ A base class for all units. """

    def __init__(self,
                 empire,
                 health: int,
                 speed: int,
                 cost: int,
                 size: Tuple[int, int],
                 image: pygame.Surface):

        base_object.GameObject.__init__(self,
                                        empire=empire,
                                        health=health,
                                        cost=cost,
                                        size=size,
                                        image=image)

        self.max_speed = speed
        self.speed = pygame.math.Vector2()
        # Convert tuple to list, so object position can be changed.
        self.cur_real_pos = list(self.rect.center)
        self.destination = self.rect.center

    def set_move_to(self, dest: Tuple[int, int]):
        """ Starts follow (move toward) the `dest` position. """
        self.destination = dest
        self._update_speed()

    def update_position(self):
        """ Tunes coordinates. The method is called after coordinates initialization. """
        self.destination = self.rect.center
        self.cur_real_pos = list(self.rect.center)

    def move(self):
        """ Makes a step toward destination. """

        previous_pos = self.rect.center
        all_intersected = pygame.sprite.Group()
        if abs(self.rect.centerx - self.destination[0]) >= self.max_speed or abs(
                self.rect.centery - self.destination[1]) >= self.max_speed:

            self.cur_real_pos[0] += self.speed.x
            self.rect.centerx = self.cur_real_pos[0]
            intersected = pygame.sprite.spritecollide(
                self, self._all_objects, dokill=False)
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
            intersected = pygame.sprite.spritecollide(
                self, self._all_objects, False)
            intersected.remove(self)
            all_intersected.add(intersected)
            for obj in intersected:
                if self.speed.y < 0:
                    self.rect.top = obj.rect.bottom
                else:
                    self.rect.bottom = obj.rect.top
                self.cur_real_pos[1] = self.rect.centery
        # If unit got stuck.
        if self.rect.center == previous_pos:
            self.action_while_stuck(all_intersected)

    def stop_move(self):
        """ If object has destination, it stops following last. """
        self.set_move_to(self.rect.center)

    # Inherited methods.
    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.set_move_to(mouse_pos)

    def info(self) -> Text:
        result = ''
        result += f'Race: {self.empire.race}\n'
        result += f'Empire: {self.empire.name}\n'
        result += f'Health: {self.health}\n'
        result += f'Speed: {self.max_speed}\n'
        return result

    def action_while_update(self):
        if self.speed.length() != 0:
            self._update_speed()
            self.move()

    # Empty methods.
    def action_while_stuck(self, intersected: pygame.sprite.Group):
        """ Is called when object gets stuck (i.e. if it should move but can't). """

    def _update_speed(self):
        self.speed = pygame.math.Vector2(self.destination) - pygame.math.Vector2(self.rect.center)
        if self.speed.length() > 0:
            self.speed.scale_to_length(self.max_speed)

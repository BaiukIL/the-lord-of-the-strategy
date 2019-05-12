import pygame
import time
from game_objects import base_object
from abc import ABC
from typing import *


def _distance_between_points(one, other) -> float:
    return pygame.Vector2(one).distance_to(pygame.Vector2(other))


class Unit(base_object.GameObject, ABC):
    def __init__(self, empire, health: int, speed: int, cost: int, size: Tuple[int, int], image: pygame.Surface):
        base_object.GameObject.__init__(self, empire=empire, health=health, cost=cost, size=size, image=image)
        self.max_speed = speed
        self.speed = pygame.Vector2()
        self.cur_real_pos = list(self.rect.center)
        self.destination = self.rect.center
        self._tmp_destination = None

    def update_position(self):
        self.destination = self.rect.center
        self.cur_real_pos = list(self.rect.center)

    def set_move_to(self, dest: Tuple[int, int]):
        self.destination = dest
        if self._tmp_destination is not None:
            self._tmp_destination = None
        self.cur_real_pos = list(self.rect.center)
        self.speed = pygame.Vector2(dest) - pygame.Vector2(self.rect.center)
        if self.speed.length() > 0:
            self.speed.scale_to_length(self.max_speed)

    def move(self):
        previous_pos = self.rect.center
        destination = self.destination
        collision_occurred = False
        collision_pos = list(self.rect.center)
        if self._tmp_destination is not None:
            self.cur_real_pos = list(self.rect.center)
            self.speed = pygame.Vector2(self._tmp_destination) - pygame.Vector2(self.rect.center)
            self.speed.scale_to_length(self.max_speed)
            destination = self._tmp_destination
        if abs(self.rect.centerx - destination[0]) >= self.max_speed or abs(
                self.rect.centery - destination[1]) >= self.max_speed:
            self.cur_real_pos[0] += self.speed.x
            self.rect.centerx = self.cur_real_pos[0]
            intersected = pygame.sprite.spritecollide(self, self._all_objects, False)
            intersected.remove(self)
            for obj in intersected:
                if self.speed.x < 0:
                    collision_pos[0] = self.rect.left = obj.rect.right
                else:
                    collision_pos[0] = self.rect.right = obj.rect.left
                self.cur_real_pos[0] = self.rect.centerx
                if self.speed.y < 0:
                    collision_pos[1] = self.rect.top
                else:
                    collision_pos[1] = self.rect.bottom
                collision_occurred = True

            self.cur_real_pos[1] += self.speed.y
            self.rect.centery = self.cur_real_pos[1]
            intersected = pygame.sprite.spritecollide(self, self._all_objects, False)
            intersected.remove(self)
            for obj in intersected:
                if self.speed.y < 0:
                    collision_pos[1] = self.rect.top = obj.rect.bottom
                else:
                    collision_pos[1] = self.rect.bottom = obj.rect.top
                self.cur_real_pos[1] = self.rect.centery
                if collision_pos[0] == self.rect.centerx:
                    if self.speed.x < 0:
                        collision_pos[0] = self.rect.left
                    else:
                        collision_pos[0] = self.rect.right
                collision_occurred = True

        if self.rect.center == previous_pos:
            if collision_occurred:
                self._tmp_destination = collision_pos
            else:
                self._tmp_destination = None

    def stop_move(self):
        self.set_move_to(self.rect.center)

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
        if self._tmp_destination is None:
            self.set_move_to(self.destination)
        if self.speed.length() != 0:
            self.move()


class Warrior(Unit):
    def __init__(self, empire, health: int, speed: int, damage: int, fight_distance: int, cost: int,
                 size: Tuple[int, int],
                 image: pygame.Surface):
        Unit.__init__(self, empire=empire, size=size, image=image, health=health, speed=speed, cost=cost)
        self.damage = damage
        self.fight_distance = fight_distance
        self.attack_target = pygame.sprite.GroupSingle()
        self.attack_delay = 3  # in seconds
        self._last_attack_call_time = time.time()

    def attack(self, obj: base_object.GameObject):
        if time.time() - self._last_attack_call_time > self.attack_delay:
            self.stop_move()
            obj.decrease_health(self.damage)
            self._last_attack_call_time = time.time()

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.attack_target.empty()
        self.set_move_to(mouse_pos)

    def handle_object_click(self, obj: base_object.GameObject):
        if obj.empire is not self.empire:
            self.attack_target.add(obj)

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        result += "Speed: {}\n".format(self.max_speed)
        result += "Damage: {}\n".format(self.damage)
        return result

    def action_while_update(self, *args):
        if self._tmp_destination is None:
            self.set_move_to(self.destination)
        for target in self.attack_target:
            if self.is_on_attack_distance_to(target):
                self.attack(target)
                return
            else:
                if self._tmp_destination is None:
                    self.set_move_to(target.rect.center)
        self.move()

    def is_on_attack_distance_to(self, target: base_object.GameObject):
        return _distance_between_points(self.rect.center, target.rect.center) < self.fight_distance


class ElfWarrior(Warrior):
    pass


class OrcWarrior(Warrior):
    pass


class DwarfWarrior(Warrior):
    pass


class Scout(Warrior):
    pass


class ElfScout(Scout):
    pass


class OrcScout(Scout):
    pass


class DwarfScout(Scout):
    pass


class Builder(Unit):
    pass


class ElfBuilder(Builder):
    pass


class OrcBuilder(Builder):
    pass


class DwarfBuilder(Builder):
    pass

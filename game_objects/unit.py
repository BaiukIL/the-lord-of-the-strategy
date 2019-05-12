import pygame
import time
from game_objects import base_object
from abc import ABC
from typing import *


class Unit(base_object.GameObject, ABC):
    def __init__(self, empire, health: int, speed: int, cost: int, size: Tuple[int, int], image: pygame.Surface):
        base_object.GameObject.__init__(self, empire=empire, health=health, cost=cost, size=size, image=image)
        self.max_speed = speed
        self.speed = pygame.Vector2()
        self.cur_real_pos = list(self.rect.center)
        self.destination = self.rect.center

    def update_position(self):
        self.destination = self.rect.center
        self.cur_real_pos = list(self.rect.center)

    def set_move_to(self, dest: Tuple[int, int]):
        self.destination = dest
        self.cur_real_pos = list(self.rect.center)
        self.speed = pygame.Vector2(dest) - pygame.Vector2(self.rect.center)
        if self.speed.length() > 0:
            self.speed.scale_to_length(self.max_speed)

    def move(self):
        previous_pos = self.cur_real_pos.copy()
        if abs(self.rect.centerx - self.destination[0]) >= self.max_speed or abs(
                self.rect.centery - self.destination[1]) >= self.max_speed:
            self.cur_real_pos[0] += self.speed.x
            self.rect.centerx = self.cur_real_pos[0]
            intersected = pygame.sprite.spritecollide(self, self._all_objects, False)
            intersected.remove(self)
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
            for obj in intersected:
                if self.speed.y < 0:
                    self.rect.top = obj.rect.bottom
                else:
                    self.rect.bottom = obj.rect.top
                self.cur_real_pos[1] = self.rect.centery
        if self.cur_real_pos == previous_pos:
            self.stop_move()

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

    def update(self, *args):
        self.set_move_to(self.destination)
        if self.speed.length() != 0:
            self.move()


class Warrior(Unit):

    def __init__(self, empire, health: int, speed: int, damage: int, cost: int, size: Tuple[int, int],
                 image: pygame.Surface):
        Unit.__init__(self, empire=empire, size=size, image=image, health=health, speed=speed, cost=cost)
        self.damage = damage
        self.attack_target = pygame.sprite.GroupSingle()
        self.attack_delay = 3  # in seconds
        self._last_attack_call_time = time.time()
        self.fight_distance = 150

    def attack(self, obj: base_object.GameObject):
        if pygame.Vector2(self.rect.center).distance_to(pygame.Vector2(obj.rect.center)) < self.fight_distance:
            self.stop_move()
            self._attack_animation()
            obj.decrease_health(self.damage)
        else:
            self.set_move_to(obj.rect.center)

    def _attack_animation(self):
        pass

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

    def update(self, *args):
        self.set_move_to(self.destination)
        for target in self.attack_target:
            if time.time() - self._last_attack_call_time > self.attack_delay:
                self.attack(target)
                self._last_attack_call_time = time.time()
        if self.speed.length() != 0:
            self.move()


class ElfWarrior(Warrior):
    pass


class OrcWarrior(Warrior):
    pass


class DwarfWarrior(Warrior):
    pass


class Scout(Unit):
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

import pygame
from game_objects import base_object
from abc import ABC
from typing import *


class Unit(base_object.GameObject, ABC):
    def __init__(self, empire, health: int, speed: int, cost: int, size: Tuple[int, int], image: pygame.Surface):
        base_object.GameObject.__init__(self, empire=empire, health=health, cost=cost, size=size, image=image)
        self.speed_val = speed
        self.vector = pygame.Vector2()
        self.cur_real_pos = list(self.rect.center)
        self.destination = self.rect.center

    def update_position(self):
        self.destination = self.rect.center
        self.cur_real_pos = list(self.rect.center)

    def set_move_to(self, mouse_pos: Tuple[int, int]):
        self.destination = mouse_pos
        self.cur_real_pos = list(self.rect.center)
        self.vector = pygame.Vector2(mouse_pos) - pygame.Vector2(self.rect.center)
        if self.vector.length() > 0:
            self.vector.scale_to_length(self.speed_val)

    def move(self):
        if not (abs(self.rect.center[0] - self.destination[0]) < 5 and
                abs(self.rect.center[1] - self.destination[1] < 5)):
            self.cur_real_pos[0] += self.vector.x
            self.cur_real_pos[1] += self.vector.y
            self.rect.center = self.cur_real_pos
            collision_occurred = False
            for sprite in pygame.sprite.spritecollide(self, self._all_objects, False):
                if sprite != self:
                    self._fix_collision()
                    collision_occurred = True
            if collision_occurred:
                self.set_move_to(self.rect.center)

    def stop_move(self):
        self.set_move_to(self.rect.center)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.set_move_to(mouse_pos)

    def info(self) -> Text:
        result = str()
        result += "Race: {}\n".format(self.empire.race)
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        result += "Speed: {}\n".format(self.speed_val)
        return result

    def update(self, *args):
        if self.vector.length() != 0:
            self.move()

    def _fix_collision(self):
        self.cur_real_pos[0] -= self.vector.x
        self.cur_real_pos[1] -= self.vector.y
        self.rect.center = self.cur_real_pos


class Warrior(Unit):

    def __init__(self, empire, health: int, speed: int, damage: int, cost: int, size: Tuple[int, int],
                 image: pygame.Surface):
        Unit.__init__(self, empire=empire, size=size, image=image, health=health, speed=speed, cost=cost)
        self.damage = damage
        self.attack_target = pygame.sprite.GroupSingle()
        self.attack_delay = 3  # in seconds
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
        result += "Speed: {}\n".format(self.speed_val)
        result += "Damage: {}\n".format(self.damage)
        return result

    def update(self, *args):
        for target in self.attack_target:
            self.attack(target)
        if self.vector.length() != 0:
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

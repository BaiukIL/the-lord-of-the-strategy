import pygame
import time
from typing import Tuple, Text
# project modules #
from game_objects.units import unit


class Warrior(unit.Unit):
    def __init__(self, empire, health: int, speed: int, damage: int, fight_distance: int, cost: int,
                 size: Tuple[int, int],
                 image: pygame.Surface):
        unit.Unit.__init__(self, empire=empire, size=size, image=image, health=health, speed=speed, cost=cost)
        self.damage = damage
        self.fight_distance = fight_distance
        self.attack_target = pygame.sprite.GroupSingle()
        self.attack_delay = 3  # in seconds
        self._last_attack_time = time.time()

    def attack(self, obj):
        if time.time() - self._last_attack_time > self.attack_delay:
            obj.decrease_health(self.damage)
            self._last_attack_time = time.time()

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.attack_target.empty()
        self.set_move_to(mouse_pos)

    def handle_object_click(self, obj):
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
        self.set_move_to(self.destination)
        for target in self.attack_target:
            if self.is_on_attack_distance_to(target):
                self.attack(target)
                return
            else:
                self.set_move_to(target.rect.center)
        self.move()

    def action_while_stuck(self, intersected: pygame.sprite.Group):
        """Choose a collided target for attack"""
        for obj in intersected:
            if obj.empire is not self.empire:
                self.attack_target.add(obj)
                return

    def is_on_attack_distance_to(self, target):
        return unit.distance_between_points(self.rect.center, target.rect.center) < self.fight_distance


class ElfWarrior(Warrior):
    pass


class OrcWarrior(Warrior):
    pass


class DwarfWarrior(Warrior):
    pass

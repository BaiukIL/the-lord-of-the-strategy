import pygame
# project modules #
import game
import singleton
import exceptions


class StressAI(metaclass=singleton.Singleton):
    def __init__(self, empire):
        self.empire = empire
        for city in self.empire.cities:
            self.main_city = city
        self.barracks = pygame.sprite.Group()
        self.mines = pygame.sprite.Group()
        self.scouts = pygame.sprite.Group()
        self.warriors = pygame.sprite.Group()
        self.init()

    def init(self):
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, 1000).center))
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, 700).center))
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, 400).center))
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, 100).center))
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, -200).center))
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, -500).center))
        self.barracks.add(
            self.main_city.build_barrack(self.main_city.rect.move(-3 * self.main_city.rect.width, -800).center))

    def play_step(self):
        try:
            for barrack in self.barracks:
                self.scouts.add(barrack.create_scout())
        except exceptions.CreationError:
            pass
        finally:
            for scout in self.scouts:
                follow_scout_strategy(scout)


def follow_scout_strategy(scout):
    if scout.attack_target.sprite is None:
        for _scout in StressAI().scouts:
            if _scout.attack_target.sprite is not None:
                scout.attack_target.add(_scout.attack_target.sprite)
                return
        for obj in game.Game().player_emp.objects:
            scout.attack_target.add(obj)

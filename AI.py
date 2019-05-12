import pygame
import time
# project modules #
import game
import singleton
import exceptions


class AI(metaclass=singleton.Singleton):
    def __init__(self, empire, create_delay: float = 2):
        self.empire = empire
        for city in self.empire.cities:
            self.main_city = city
        self.barracks = pygame.sprite.Group()
        self.mines = pygame.sprite.Group()
        self.scouts = pygame.sprite.Group()
        self.warriors = pygame.sprite.Group()
        self._create_delay = create_delay
        self._previous_unit_creation = 0
        self.init()

    def init(self):
        self.mines.add(self.main_city.build_mine(self.main_city.rect.move(0, -3*self.main_city.rect.width).center))
        self.mines.add(self.main_city.build_mine(self.main_city.rect.move(0, 3*self.main_city.rect.width).center))
        self.mines.add(self.main_city.build_mine(self.main_city.rect.move(3*self.main_city.rect.width, 0).center))
        self.barracks.add(self.main_city.build_barrack(self.main_city.rect.move(-3*self.main_city.rect.width, 0).center))

    def play_step(self):
        try:
            if time.time() - self._previous_unit_creation > self._create_delay:
                self._previous_unit_creation = time.time()
                for barrack in self.barracks:
                    self.scouts.add(barrack.create_scout())
        except exceptions.CreationError:
            pass
        finally:
            for scout in self.scouts:
                follow_scout_strategy(scout)


def follow_scout_strategy(scout):
    if scout.attack_target.sprite is None:
        for _scout in AI().scouts:
            if _scout.attack_target.sprite is not None:
                scout.attack_target.add(_scout.attack_target.sprite)
                return
        for obj in game.Game().player_emp.objects:
            scout.attack_target.add(obj)

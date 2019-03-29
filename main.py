"""
Color: 546E7A
Fabric class : RaceFactory.
Problem:
There are different units in game, but they have number of similar methods like:
 - Create
 - Health
 - Damage
 - Die ... and it isn't necessary for other game objects to interact to specific unit instance
Solution:
 * Derive specific unit classes from Unit (which have common for units methods and fields)
Conditionality:
 1. it allows to add new units in the game with no refactoring of existing code. Thus game becomes easily expandable
Remember:
!!! Every unit object of the game should be referenced as Unit object and no specific instances of Unit must be used
----------------------------------------------------------------------------------
    There are 3 empires in game:
     - ElfEmpire
     - OrcEmpire
     - DwarfEmpire
    It's clear that they should be produced from Abstract factory. Indeed, once player has chosen concreteEmpire he must
    not have an ability to create other Races' stuff. However, they have absolutely similar fields and methods so
    difference between them can't be notices so far on this level of abstraction (but it does exist on next levels).
    It causes a problem of code extension: every time we want to add a new Race we have to copy abstract level
    in order to save Abstract factory's principle.
"""


from collections import defaultdict
import logging
logging.basicConfig(level=logging.INFO)


class Prototype:
    def clone(self):
        raise NotImplementedError


class Race:
    def skill(self):
        raise NotImplementedError


class Elf(Race):
    pass


class Orc(Race):
    pass


class Dwarf(Race):
    pass


races = {Elf, Dwarf, Orc}


class Empire:
    def __init__(self, race):
        if race in races:
            self.race = race
        else:
            raise KeyError("Unknown race: {}".format(race))
        self.army = Army(self.race)
        self.cities = defaultdict(City)
        logging.info("{}Empire has created".format(self.race.__name__))

    def get_city(self, name):
        if name in self.cities:
            return self.cities.get(name)
        else:
            raise KeyError("{} city doesn't exist in {}Empire".format(name, self.race.__name__))

    def get_army(self):
        return self.army

    def what_race(self):
        return self.race.__name__

    def establish_city(self, name):
        if name not in self.cities:
            self.cities[name] = City(self.race, name)
            logging.info("{}Empire has established city: {}".format(self.race.__name__, name))
        else:
            raise KeyError("City {} has already exists in {} cities".format(name, self.race.__name__))


#
# # factory returns exact Race factory
# class RaceAbstractFactory:
#     @staticmethod
#     def create(race):
#         if race is Dwarf:
#             logging.info("DwarfEmpire factory created")
#             return DwarfEmpire()
#         elif race is Elf:
#             logging.info("ElfEmpire factory created")
#             return ElfEmpire()
#         elif race is Orc:
#             logging.info("OrcEmpire factory created")
#             return OrcEmpire()
#         else:
#             logging.error("Unknown race - can't create factory")
#
#
# class Empire:
#     def __init__(self):
#         self.army = list()
#         self.cities = list()
#
#     def create_city(self, name):
#         pass
#
#
# class ElfEmpire(Empire):
#     pass
#
#
# class OrcEmpire(Empire):
#     pass
#
#
# class DwarfEmpire(Empire):
#     pass

# "Composite" pattern in the future
class Army:
    def __init__(self, race):
        self.units = list()
        self.race = race

    def info(self):
        print("Army race: {}".format(self.race.__name__))
        print("Army units:")
        for unit in self.units:
            print(" - {}".format(unit))

    def _add_unit(self, unit):
        self.units.append(unit)
        logging.info("{} has joined to {}Empire army".format(unit, self.race.__name__))


# class ElfArmy(Army):
#     pass
#
#
# class OrcArmy(Army):
#     pass
#
#
# class DwarfArmy(Army):
#     pass


class City:
    def __init__(self, race, name):
        self.race = race
        self.name = name
        self.buildings = list()
        if self.race is Elf:
            self.factory = ElfBuildingFactory()
        elif self.race is Orc:
            self.factory = OrcBuildingFactory()
        elif self.race is Dwarf:
            self.factory = DwarfBuildingFactory()
        else:
            raise Exception("Unknown race: {}".format(race))

    def info(self):
        print("City race: {}".format(self.race.__name__))
        print("City name: {}".format(self.name))
        if len(self.buildings) == 0:
            print("There're no buildings in this city")
        else:
            print("City buildings:")
            for building in self.buildings:
                print(" - {}".format(building.__class__.__name__))

    def build_barrack(self, strength):
        self.buildings.append(self.factory.build_barrack(strength))

    def build_mine(self, strength):
        self.buildings.append(self.factory.build_mine(strength))

    def build_wall(self, strength):
        self.buildings.append(self.factory.build_wall(strength))


# it is interface because it's used in Unit and Building classes
class Health:
    def __init__(self, health):
        self.health = health
        if not self.is_alive():
            raise Exception("Can't create object with negative or zero health")

    def increase_health(self, health):
        self.health += health

    def decrease_health(self, damage):
        self.health -= damage
        if not self.is_alive():
            self._destroy()

    def is_alive(self):
        return self.health > 0

    def _destroy(self):
        raise NotImplementedError


class Speed:
    def __init__(self, speed):
        self.speed = speed

    def decrease_speed(self, value):
        if value >= 0:
            self.speed += value
        else:
            raise KeyError("Can't decrease negative speed: {}. Use decrease_speed for this".format(value))

    def increase_speed(self, value):
        if value >= 0:
            self.speed += value
        else:
            raise KeyError("Can't add negative speed: {}. Use decrease_speed for this".format(value))


# Most units and buildings are supposed to be created many times without any difference,
# thus it's good idea to clone them



# abstract factory of races' factories
class RaceBuildingFactory:
    def build_barrack(self, strength):
        raise NotImplementedError

    def build_mine(self, strength):
        raise NotImplementedError

    def build_wall(self, strength):
        raise NotImplementedError


# factory of Elves' buildings
class ElfBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
        return ElfBarrack(strength)

    def build_mine(self, strength):
        return ElfMine(strength)

    def build_wall(self, strength):
        return ElfWall(strength)


# factory of Orcs' buildings
class OrcBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
        return OrcBarrack(strength)

    def build_mine(self, strength):
        return OrcMine(strength)

    def build_wall(self, strength):
        return OrcWall(strength)


# factory of Dwarfs' buildings
class DwarfBuildingFactory(RaceBuildingFactory):
    def build_barrack(self, strength):
        return DwarfBarrack(strength)

    def build_mine(self, strength):
        return DwarfMine(strength)

    def build_wall(self, strength):
        return DwarfWall(strength)


class Building(Health):
    def __init__(self, strength):
        Health.__init__(self, strength)
        logging.info("{} is created".format(self.__class__.__name__))

    def update(self):
        pass
        logging.info("{} has been updated!".format(self.__class__.__name__))

    def _destroy(self):
        pass
        logging.info("{} has been destroyed".format(self.__class__.__name__))


# fabric of units
class Barrack(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def create_scout(self, ):
        raise NotImplementedError

    def create_builder(self):
        raise NotImplementedError

    def create_warrior(self):
        raise NotImplementedError


# fabric of elf units
class ElfBarrack(Barrack):
    def __init__(self, strength):
        Barrack.__init__(self, strength)

    def create_scout(self, ):
        return

    def create_builder(self):
        return

    def create_warrior(self):
        return


# fabric of orc units
class OrcBarrack(Barrack):
    def __init__(self, strength):
        Barrack.__init__(self, strength)

    def create_scout(self):
        return

    def create_builder(self):
        return

    def create_warrior(self):
        return


# fabric of dwarf units
class DwarfBarrack(Barrack):
    def __init__(self, strength):
        Barrack.__init__(self, strength)

    def create_scout(self, ):
        return

    def create_builder(self):
        return

    def create_warrior(self):
        return


class Mine(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def mine(self):
        logging.info("{} is mining".format(self.__class__.__name__))


class ElfMine(Mine):
    def __init__(self, strength):
        Mine.__init__(self, strength)


class OrcMine(Mine):
    def __init__(self, strength):
        Mine.__init__(self, strength)


class DwarfMine(Mine):
    def __init__(self, strength):
        Mine.__init__(self, strength)


class Wall(Building):
    def __init__(self, strength):
        Building.__init__(self, strength)

    def update(self):
        pass
        logging.info("{} is updated".format(self.__class__.__name__))


class ElfWall(Wall):
    def __init__(self, strength):
        Wall.__init__(self, strength)


class OrcWall(Wall):
    def __init__(self, strength):
        Wall.__init__(self, strength)


class DwarfWall(Wall):
    def __init__(self, strength):
        Wall.__init__(self, strength)


def play_game():
    player1 = Empire(Dwarf)
    player1.establish_city('Turden')

    city = player1.get_city('Turden')
    city.build_barrack(10)
    city.build_mine(3)
    city.build_wall(1)
    city.info()


if __name__ == '__main__':
    play_game()
# def check_car_borders(x, y):
#     if x < 0:
#         x = 0
#         message_display("Can't move left")
#     if y < 0:
#         y = 0
#         message_display("Can't move up")
#
#
# def draw_square(x, y, width, height, speed):
#     pygame.draw.rect(gameDisplay, red, [x, y, width, height])
#     y -= speed
#
#
# def message_display(text):
#     font = pygame.font.Font('freesansbold.ttf', 50)
#     TextSurface = font.render(text, True, red)
#     TextRect = TextSurface.get_rect()
#     TextRect.center = (display_width/2, display_height/2)
#     gameDisplay.blit(TextSurface, TextRect)
#     pygame.display.update()
#     time.sleep(0.5)


# clock = pygame.time.Clock()


# This class is necessary for the following reason.
# There's a problem: when we use self.matrix[x][y] it means we appeal to y symbol in x string. However, we'd like
# to appeal to x symbol in y string what corresponds to our acceptance of using such expressions. Thus, we
# need a class with overloaded [] operator: [x][y] --> [y][x]
# class Matrix:
#     def __init__(self, width, height):
#         self.mat =
#
#     def __getitem__(self, item):
#
#         return
# from functools import wraps
# decorator
# def once(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         wrapper.called = False
#         result = None
#         if not wrapper.called:
#             result = function(*args, **kwargs)
#         wrapper.called = True
#         return result
#     return wrapper

# decorator which allows to call function only in the way "seconds" time is passed after previous call
# return pass-function (do nothing) if function can't be called
# def action_frequency_limit(seconds):
#     def wrapper(func):
#         def pass_func():
#             pass
#
#         @wraps(func)
#         def wrap(*args, **kwargs):
#             if time.time() - wrap.last_time_called >= seconds or not wrap.called:
#                 wrap.called = True
#                 wrap.last_time_called = time.time()
#                 wrap()
#                 return func(*args, **kwargs)
#             else:
#                 return pass_func
#
#         wrap.last_time_called = time.time()
#         wrap.called = False
#         return wrap
#     return wrapper


# def second_game_loop():
#     while True:
#         draw_objects()
#         this_game.field.update()
#
#         for player in this_game.players:
#             if player.kind is gameconst_.USER:
#                 act = None
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
#                         pygame.quit()
#                         quit()
#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_a:
#                             act = 'a'
#                         elif event.key == pygame.K_d:
#                             act = 'd'
#                         elif event.key == pygame.K_w:
#                             act = 'w'
#                         elif event.key == pygame.K_s:
#                             act = 's'
#                         print(event)
#                 time.sleep(0.1)
#                 player.tank.move(act)
#             elif player.kind is gameconst_.ENEMY:
#                 player.tank.move(player.next_step)

# class Vector:
#     name = "flat"
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __abs__(self):
#         return (self.x**2 + self.y**2)**.5
#
#     def __str__(self):
#         return "{} {}".format(self.x, self.y)
#
#     def __call__(self, *args, **kwargs):
#         print("I've been called!")

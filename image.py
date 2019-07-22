""" This module contains race-dependent image classes and `get_image` function.
Usage example:

warrior = OrcWarrior(...)

img = image.get_image(warrior.empire).WARRIOR

Now `img` is `pygame.Surface` which represents orc warrior image. """


import pygame
# project modules #
import singleton
from game_objects import races


# TODO: why it takes `empire` instead of race?
def get_image(empire=None):
    """ Returns appropriate race image class. """

    # If no empire is specified, returns race-independent images.
    if empire is None:
        return ImageProxy()
    if empire.race == races.ELVES:
        return ElvesImages()
    if empire.race == races.ORCS:
        return OrcsImages()
    if empire.race == races.DWARFS:
        return DwarfsImages()
    raise ImageError(f'{empire} object is not empire instance.')


# TODO: Make Proxy classes enumerations.
class ImageProxy(metaclass=singleton.Singleton):
    """ Contains general (race-independent) images. """

    def __init__(self):
        for member in dir(self):
            if not callable(member) and not member.startswith("__"):
                setattr(self, member, pygame.image.load(
                    f'images/{getattr(self, member)}').convert_alpha())

    ICON = 'icon.jpeg'
    BUILD = 'build icon.png'
    REMOVE = 'destroy icon.png'
    UPGRADE = 'upgrade icon.png'


class ElvesImages(ImageProxy):
    """ Contains general (race-independent) and elves images. """

    EMPIRE_ICON = 'elves empire icon.png'
    CITY = 'elves city.png'
    BARRACK = 'elves barrack.png'
    MINE = 'elves mine.png'
    WALL = 'elves wall.png'
    BUILDER = 'elves builder.png'
    SCOUT = 'elves scout.png'
    WARRIOR = 'elves warrior.png'


class OrcsImages(ImageProxy):
    """ Contains general (race-independent) and orcs images. """

    EMPIRE_ICON = 'orcs empire icon.png'
    CITY = 'orcs city.png'
    BARRACK = 'orcs barrack.png'
    MINE = 'orcs mine.png'
    WALL = 'orcs wall.png'
    BUILDER = 'orcs builder.png'
    SCOUT = 'orcs scout.png'
    WARRIOR = 'orcs warrior.png'


class DwarfsImages(ImageProxy):
    """ Contains general (race-independent) and dwarfs images. """

    EMPIRE_ICON = 'dwarfs empire icon.png'
    CITY = 'dwarfs city.png'
    BARRACK = 'dwarfs barrack.png'
    MINE = 'dwarfs mine.png'
    WALL = 'dwarfs wall.png'
    BUILDER = 'dwarfs builder.png'
    SCOUT = 'dwarfs scout.png'
    WARRIOR = 'dwarfs warrior.png'


class ImageError(Exception):
    pass

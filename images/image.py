"""PROXY!!!"""


import pygame
from game_objects import races
import templates


def get_image(empire=None):
    """
    If no object specified, returns race-independent images"""
    if empire is None:
        return ImageProxy()
    elif empire.race == races.ELVES:
        return ElvesImages()
    elif empire.race == races.ORCS:
        return OrcsImages()
    elif empire.race == races.DWARFS:
        return DwarfsImages()


class ImageProxy(metaclass=templates.Singleton):
    def __init__(self):
        for member in dir(self):
            if not callable(member) and not member.startswith("__"):
                setattr(self, member, pygame.image.load('images/sources/{}'.format(getattr(self, member))))
    
    ICON = 'icon.jpeg'
    BUILD = 'build icon.png'
    REMOVE = 'destroy icon.png'
    UPGRADE = 'upgrade icon.png'
    
    
class ElvesImages(ImageProxy):
    CITY = 'elves city.png'
    BARRACK = 'elves barrack.png'
    MINE = 'elves mine.png'
    WALL = 'elves wall.png'
    BUILDER = 'elves builder.png'
    SCOUT = 'elves scout.png'
    WARRIOR = 'elves warrior.png'
    

class OrcsImages(ImageProxy):
    CITY = 'orcs city.png'
    BARRACK = 'orcs barrack.png'
    MINE = 'orcs mine.png'
    WALL = 'orcs wall.png'
    BUILDER = 'orcs builder.png'
    SCOUT = 'orcs scout.png'
    WARRIOR = 'orcs warrior.png'

    
class DwarfsImages(ImageProxy):
    CITY = 'dwarfs city.png'
    BARRACK = 'dwarfs barrack.png'
    MINE = 'dwarfs mine.png'
    WALL = 'dwarfs wall.png'
    BUILDER = 'dwarfs builder.png'
    SCOUT = 'dwarfs scout.png'
    WARRIOR = 'dwarfs warrior.png'

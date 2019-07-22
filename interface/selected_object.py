""" This module contains `SelectedObject` which keeps track of last choosen (selected) object. """


import pygame


class SelectedObject:
    """ Keeps track of last choosen (selected) object. """

    def __init__(self):
        self._object = pygame.sprite.GroupSingle()

    def get(self):
        """ Returns selected object if it exists or `None` otherwise. """
        for obj in self._object:
            return obj
        return None

    def replace(self, new_object):
        """ Replace current object with `new_object`. """
        for old_object in self._object:
            old_object.interact_with(new_object)
            old_object.passive()
        self._object.add(new_object)
        new_object.active()

    def clear(self):
        """ Clear selected object (i.e. there is no selected object after this action). """
        for obj in self._object:
            obj.passive()
        self._object.empty()

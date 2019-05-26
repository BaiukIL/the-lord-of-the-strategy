import pygame
# project modules #


class SelectedObject:
    def __init__(self):
        self._object = pygame.sprite.GroupSingle()

    def get(self):
        for obj in self._object:
            return obj
        return None

    def replace(self, new_object):
        for old_object in self._object:
            old_object.interact_with(new_object)
            old_object.passive()
        self._object.add(new_object)
        new_object.active()

    def clear(self):
        for obj in self._object:
            obj.passive()
        self._object.empty()

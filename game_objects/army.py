""" This module contains `Army` which s responsible for units hierarchy. """


import collections
from abc import ABC, abstractmethod
from game_objects.units import unit as unit_mod

# Army is based on wide-spread Composite & Iterator & Visitor pattern.

# Composite.
class ArmyComponent(ABC):

    _parent: 'ArmyComponent'

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value: 'ArmyComponent'):
        self._parent = value

    @property
    @abstractmethod
    def groups(self) -> list:
        pass

    def get_unit(self) -> unit_mod.Unit:
        pass

    def is_compound(self) -> bool:
        return True


class ArmyComposite(ArmyComponent):

    _groups: list

    def __init__(self):
        self._groups = list()

    def __iter__(self) -> 'ArmyIterator':
        return ArmyIterator(self)

    @property
    def groups(self) -> list:
        return self._groups

    def add(self, component: ArmyComponent):
        self._groups.append(component)
        component.parent = self

    def remove(self, component):
        self._groups.remove(component)


class ArmyLeaf(ArmyComponent):
    def __init__(self, unit: unit_mod.Unit):
        self._unit = unit

    @property
    def groups(self) -> list:
        """returns empty list, for there are no children"""
        return list()

    def get_unit(self) -> unit_mod.Unit:
        return self._unit

    def is_compound(self) -> bool:
        return False


# Iterator.
class ArmyIterator(collections.abc.Iterator):

    _queue: collections.deque
    _position: ArmyComponent

    def __init__(self, collection: ArmyComponent):
        self._position = collection
        self._queue = collections.deque()
        self._queue.append(collection)

    def __next__(self) -> ArmyComponent:
        try:
            self._position = self._queue.popleft()
            for child in self._position.groups:
                self._queue.append(child)
        except IndexError:
            raise StopIteration
        return self._position


# Visitor.
class Army:
    """ Army rules with units and lets to group them in troops. """

    def __init__(self, empire):
        self.empire = empire
        self._army = ArmyComposite()

    def info(self):
        print("Empire: {}".format(self.empire.name))
        print("Race: {}".format(self.empire.race))
        print("Army consists of:")
        for group in self._army:
            if not group.is_compound():
                group.get_unit().info()

    def recruit_unit(self, unit: unit_mod.Unit):
        self._army.add(ArmyLeaf(unit))

    def remove_group(self, group: ArmyComponent):
        for component in self._army:
            if component is group:
                component.parent.remove(component)
                break

    def size(self) -> int:
        result = 0
        for component in self._army:
            if not component.is_compound():
                result += 1
        return result

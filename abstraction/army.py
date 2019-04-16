"""Composite & Iterator & Visitor"""

from abstraction import gameobject
from abstraction.units import unit as unit_mod
import collections
from abc import ABC, abstractmethod


# composite
class ArmyComponent(ABC):
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    @abstractmethod
    def groups(self) -> list:
        raise NotImplementedError

    def get_unit(self) -> unit_mod.Unit:
        pass

    def is_compound(self) -> bool:
        return True


# iterator
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


class ArmyComposite(ArmyComponent):
    _groups: list

    def __init__(self):
        self._groups = list()

    def __iter__(self) -> ArmyIterator:
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


# visitor
class Army(gameobject.GameObject):
    def __init__(self, empire):
        gameobject.GameObject.__init__(self, race=empire.race)
        self._master_empire = empire
        self._army = ArmyComposite()

    def info(self):
        print("Army's empire: {}".format(self._master_empire.name))
        print("Army's race: {}".format(self._race))
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

from abc import ABC, abstractmethod


class HealthError(Exception):
    pass


class Health(ABC):
    _health: int

    def __init__(self, health: int):
        self._health = health
        if not self.is_alive():
            raise HealthError("Can't create object with negative or zero health: {}".format(health))

    @property
    def health(self):
        return self._health

    def increase_health(self, value: int):
        if value >= 0:
            self._health += value
        else:
            raise HealthError("Can't increase negative health: {}. Use decrease_health for this".format(value))

    def decrease_health(self, value: int):
        if value >= 0:
            self._health -= value
        else:
            raise HealthError("Can't decrease negative health: {}. Use increase_health for this".format(value))
        if not self.is_alive():
            self._destroy()

    def is_alive(self):
        return self._health > 0

    @abstractmethod
    def _destroy(self):
        pass

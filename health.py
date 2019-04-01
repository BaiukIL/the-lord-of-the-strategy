from abc import abstractmethod


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

    @abstractmethod
    def _destroy(self):
        pass

class Health:
    health: int

    def set_health(self, health: int):
        self.health = health
        if not self.is_alive():
            raise Exception("Can't create object with negative or zero health: {}".format(health))

    def increase_health(self, value: int):
        if value > 0:
            self.health += value
        else:
            raise KeyError("Can't increase negative health: {}. Use decrease_health for this".format(value))

    def decrease_health(self, value: int):
        if value > 0:
            self.health -= value
        else:
            raise KeyError("Can't decrease negative health: {}. Use increase_health for this".format(value))
        if not self.is_alive():
            self._destroy()

    def is_alive(self):
        return self.health > 0

    def _destroy(self):
        raise NotImplementedError

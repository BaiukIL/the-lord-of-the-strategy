class SpeedError(Exception):
    pass


class Speed:
    _speed: int

    def __init__(self, speed: int):
        self._speed = speed
        if not self.can_move():
            self._speed = 0

    @property
    def speed(self):
        return self._speed

    def increase_speed(self, value: int):
        if value >= 0:
            self._speed += value
        else:
            raise SpeedError("Can't increase negative speed: {}. Use decrease_speed for this".format(value))

    def decrease_speed(self, value: int):
        if value >= 0:
            self._speed -= value
        else:
            raise SpeedError("Can't decrease negative speed: {}. Use increase_speed for this".format(value))
        if not self.can_move():
            self._speed = 0

    def can_move(self):
        return self._speed > 0

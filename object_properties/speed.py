class Speed:
    speed: int

    def set_speed(self, speed: int):
        self.speed = speed
        if not self.can_move():
            self.speed = 0

    def increase_speed(self, value: int):
        if value >= 0:
            self.speed += value
        else:
            raise KeyError("Can't add negative speed: {}. Use decrease_speed for this".format(value))

    def decrease_speed(self, value: int):
        if value >= 0:
            self.speed -= value
        else:
            raise KeyError("Can't decrease negative speed: {}. Use decrease_speed for this".format(value))
        if not self.can_move():
            self.speed = 0

    def can_move(self):
        return self.speed > 0

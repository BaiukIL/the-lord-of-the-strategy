class Speed:
    def __init__(self, speed):
        self.speed = speed

    def decrease_speed(self, value):
        if value >= 0:
            self.speed += value
        else:
            raise KeyError("Can't decrease negative speed: {}. Use decrease_speed for this".format(value))

    def increase_speed(self, value):
        if value >= 0:
            self.speed += value
        else:
            raise KeyError("Can't add negative speed: {}. Use decrease_speed for this".format(value))

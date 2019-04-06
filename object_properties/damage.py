class Damage:
    damage: int

    def set_damage(self, damage: int):
        self.damage = damage
        if not self.can_hit():
            self.damage = 0

    def increase_damage(self, value: int):
        if value >= 0:
            self.damage += value
        else:
            raise KeyError("Can't decrease negative speed: {}. Use decrease_damage for this".format(value))

    def decrease_damage(self, value: int):
        if value >= 0:
            self.damage -= value
        else:
            raise KeyError("Can't decrease negative speed: {}. Use increase_damage for this".format(value))
        if not self.can_hit():
            self.damage = 0

    def can_hit(self):
        return self.damage > 0

    def hit(self, obj):
        obj.decrease_health(self.damage)



class Damage:
    _damage: int

    def __init__(self, damage: int):
        self._damage = damage
        if not self.can_hit():
            self._damage = 0

    @property
    def damage(self):
        return self._damage

    def increase_damage(self, value: int):
        if value >= 0:
            self._damage += value
        else:
            raise DamageError("Can't increase negative damage: {}. Use decrease_damage for this".format(value))

    def decrease_damage(self, value: int):
        if value >= 0:
            self._damage -= value
        else:
            raise DamageError("Can't decrease negative damage: {}. Use increase_damage for this".format(value))

        if not self.can_hit():
            self._damage = 0

    def can_hit(self):
        return self._damage > 0

    def hit(self, obj):
        obj.decrease_health(self._damage)


class DamageError(Exception):
    pass

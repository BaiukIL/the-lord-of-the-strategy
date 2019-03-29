class Damage:
    def __init__(self, damage):
        self.damage = damage

    def hit(self, obj):
        obj.decrease_health(self.damage)

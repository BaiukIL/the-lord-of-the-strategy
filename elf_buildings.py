import building
import unit


# fabric of elf units
class ElfBarrack(building.Barrack):
    def create_scout(self):
        scout = unit.Unit(1, 1)
        # elf scout creation
        self.add_unit_to_army(scout)

    def create_builder(self):
        builder = unit.Unit(1, 1)
        # elf builder creation
        self.add_unit_to_army(builder)

    def create_warrior(self):
        warrior = unit.Unit(1, 1)
        # elf warrior creation
        self.add_unit_to_army(warrior)


class ElfMine(building.Mine):
    def __init__(self, strength):
        building.Mine.__init__(self, strength)


class ElfWall(building.Wall):
    def __init__(self, strength):
        building.Wall.__init__(self, strength)

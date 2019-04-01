import building
import unit


# fabric of dwarf units
class DwarfBarrack(building.Barrack):
    def create_scout(self):
        scout = unit.Unit(1, 1)
        # dwarf scout creation
        self.add_unit_to_army(scout)

    def create_builder(self):
        builder = unit.Unit(1, 1)
        # dwarf builder creation
        self.add_unit_to_army(builder)

    def create_warrior(self):
        warrior = unit.Unit(1, 1)
        # dwarf warrior creation
        self.add_unit_to_army(warrior)


class DwarfMine(building.Mine):
    def __init__(self, strength):
        building.Mine.__init__(self, strength)


class DwarfWall(building.Wall):
    def __init__(self, strength):
        building.Wall.__init__(self, strength)

import building
import unit


# fabric of orc units
class OrcBarrack(building.Barrack):
    def create_scout(self):
        scout = unit.Unit(1, 1)
        # orc scout creation
        self.add_unit_to_army(scout)

    def create_builder(self):
        builder = unit.Unit(1, 1)
        # orc builder creation
        self.add_unit_to_army(builder)

    def create_warrior(self):
        warrior = unit.Unit(1, 1)
        # orc warrior creation
        self.add_unit_to_army(warrior)


class OrcMine(building.Mine):
    def __init__(self, strength):
        building.Mine.__init__(self, strength)


class OrcWall(building.Wall):
    def __init__(self, strength):
        building.Wall.__init__(self, strength)

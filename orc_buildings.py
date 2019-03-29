import building


# fabric of orc units
class OrcBarrack(building.Barrack):
    def __init__(self, strength):
        building.Barrack.__init__(self, strength)

    def create_scout(self):
        return

    def create_builder(self):
        return

    def create_warrior(self):
        return


class OrcMine(building.Mine):
    def __init__(self, strength):
        building.Mine.__init__(self, strength)


class OrcWall(building.Wall):
    def __init__(self, strength):
        building.Wall.__init__(self, strength)

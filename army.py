import logging


class Army:
    def __init__(self, race, empire):
        self.race = race
        self.master_empire = empire
        self.troops = list()

    def info(self):
        print("Army race: {}".format(self.race.__name__))
        print("Army units:")
        for troop in self.troops:
            for unit in troop.get_all_units():
                print(" - {}".format(unit))

    def recruit(self, unit):
        troop = ArmyComposite()
        troop.add(ArmyLeaf(unit))
        self.troops.append(troop)
        logging.info("{} has joined to {}Empire army".format(troop, self.race.__name__))

    def group_selected(self, troop, other_troop):
        troop.add(other_troop)
        self.troops.remove(other_troop)


# Composite pattern
class ArmyComponent:
    def get_all_units(self):
        pass

    def size(self):
        pass

    def is_compound(self):
        pass


class ArmyComposite(ArmyComponent):
    def __init__(self):
        self.groups = list()

    def add(self, group):
        self.groups.append(group)

    def remove(self, element):
        for group in self.groups:
            if group is element:
                self.groups.remove(element)
                return
            if group.is_compound():
                group.remove()

    def get_all_units(self):
        total = list()
        for subgroup in self.groups:
            total.extend(subgroup.get_all_units())
        return total

    def size(self):
        result = 0
        for subgroup in self.groups:
            result += subgroup.size()
        return result

    def is_compound(self):
        return True


class ArmyLeaf(ArmyComponent):
    def __init__(self, obj):
        self.obj = obj

    def get_all_units(self):
        return self.obj

    def size(self):
        return 1

    def is_compound(self):
        return False
